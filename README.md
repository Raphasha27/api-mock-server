# 👻 api-mock-server (Ghost)
![Health-Hub](https://img.shields.io/badge/Health--Hub-%E2%9C%94-00D1FF?style=flat-square)

**Ghost** is an instant mock API engine that turns any OpenAPI (Swagger) specification into a live, local mock server in seconds. It bridges the gap between frontend and backend development by allowing teams to test against realistic API responses before the real service is built.

## 🚀 Features

-   **⚡ Instant Serving**: One command to turn `yaml` or `json` specs into a live FastAPI server.
-   **🔄 Dynamic Mocking**: Automatically extracts examples and schemas from your spec to generate responses.
-   **🛠️ Developer-First**: Lightweight, zero-config, and designed for local frontend development.
-   **🐳 Docker Ready**: Easily containerize your mock server for shared staging environments.

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Raphasha27/api-mock-server.git
cd api-mock-server

# Install dependencies
pip install typer fastapi uvicorn PyYAML
```

## ⌨️ Usage

### Spin up your mock server
```bash
python ghost.py serve ./openapi.yaml
```

### Test the mock
Once running, you can access your endpoints at `http://localhost:8080`.

---
*Built with ❤️ by Koketso Raphasha using DevForge AI.*
