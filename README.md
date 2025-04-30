# 🧭 GIS Starter with Redis & Python (DevContainer)

This project provides a preconfigured development environment to work with Redis and Python — ideal for geospatial projects, workshops, or classes using GitHub Codespaces or Visual Studio Code with the Dev Containers extension.

## 🚀 Features

- 🧠 **Redis**: In-memory key-value database for fast data access.
- 🖥️ **RedisInsight**: Graphical interface to explore and manage Redis data.
- 🐍 **Python 3** with libraries to interact with Redis.
- ⚙️ DevContainer setup for reproducible development environments.

## 🧰 Technologies Used

- [Redis](https://redis.io/)
- [RedisInsight](https://redis.com/redis-enterprise/redis-insight/)
- [Python 3](https://www.python.org/)
- [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/)
- [Visual Studio Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [GitHub Codespaces](https://github.com/features/codespaces) (optional)

## 🛠️ Requirements

- [Docker](https://www.docker.com/) installed on your machine
- [Visual Studio Code](https://code.visualstudio.com/) with the Dev Containers extension
- A GitHub account for using Codespaces (optional)

## 🚀 Quick Start

### 🔁 Clone the Repository

```bash
git clone https://github.com/voirinprof/gis_starter_redis_geolab.git
cd gis_starter_redis_geolab
```

### 🐳 Open in a DevContainer

1. Open the folder in Visual Studio Code.
2. When prompted, click “Reopen in Container.”
3. Wait for the environment to build and initialize.

### 💻 Or Use GitHub Codespaces

1. Click the green **"Code"** button on the GitHub repo.
2. Choose **"Open with Codespaces"** > **"New codespace"**.
3. The environment will be ready in a few minutes.

## 📂 Project Structure

```
gis_starter_redis_geolab/
├── .devcontainer/
│   ├── devcontainer.json
│   ├── requirements.txt
│   ├── Dockerfile
│   └── docker-compose.yml
├── scripts/
│   └── ... some scripts in Python to exchange with Redis
└── README.md
```

- `.devcontainer/`: Development environment configuration
- `scripts/`: Python source code directory

## 🧪 RedisInsight

You can use `RedisInsight` in your browser. Go to tab `foward ports`, click on the port `5540` and open in browser. You should add the database : `redis` (instead localhost)

## 📚 Useful Resources

- [Redis Documentation](https://redis.io/docs/)
- [RedisInsight Guide](https://docs.redis.com/latest/ri/)
- [VS Code Dev Containers Guide](https://code.visualstudio.com/docs/devcontainers/containers)
- [GitHub Codespaces Intro](https://docs.github.com/en/codespaces)

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to improve this project.