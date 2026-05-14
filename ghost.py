import typer
import yaml
import json
import uvicorn
from fastapi import FastAPI
from rich.console import Console

app = typer.Typer(help="API-Mock-Server: Instant mock APIs from OpenAPI specs.")
console = Console()

def create_mock_app(spec_data: dict):
    mock_app = FastAPI(title="Ghost Mock Server")
    
    # Simple logic to create endpoints from spec
    # This is a basic version that just mocks the structure
    paths = spec_data.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            responses = details.get("responses", {})
            success_response = responses.get("200", {}).get("content", {}).get("application/json", {}).get("example", {"status": "mocked"})
            
            # Use a factory to create the handler
            def create_handler(resp=success_response):
                async def handler():
                    return resp
                return handler
            
            # Register the route
            endpoint_name = f"{method}_{path.replace('/', '_')}"
            mock_app.add_api_route(path, create_handler(), methods=[method.upper()], name=endpoint_name)
            
    return mock_app

@app.command()
def serve(spec: str = typer.Argument(..., help="Path to OpenAPI spec (YAML or JSON)")):
    """
    Spins up a live mock server based on your API specification.
    """
    console.print(f"[bold blue]👻 Ghost is loading spec from {spec}...[/bold blue]")
    
    try:
        with open(spec, 'r') as f:
            if spec.endswith('.yaml') or spec.endswith('.yml'):
                spec_data = yaml.safe_load(f)
            else:
                spec_data = json.load(f)
                
        mock_app = create_mock_app(spec_data)
        console.print("[bold green]🚀 Mock server ready! Serving on http://localhost:8080[/bold green]")
        uvicorn.run(mock_app, host="0.0.0.0", port=8080)
        
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    app()
