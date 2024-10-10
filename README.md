# WebSocket 服务器项目

这是一个高性能的 WebSocket 服务器项目，具备高可扩展性、高可用性和国际化支持。该项目基于实时更新，确保服务的稳定性和高效性。

## 特性

- **高扩展性**：模块化设计，方便功能扩展和维护，支持实时更新。
- **高可用性**：优化的连接管理和错误日志记录，保证服务的稳定性和实时更新。
- **性能监控**：集成 Prometheus，提供关键指标的实时监控和更新。
- **Redis 支持**：使用异步 Redis 客户端，高效获取数据，并支持实时更新。
- **配置灵活**：支持环境变量和配置文件，方便部署和配置，并支持实时更新。

## 快速开始

### 先决条件

- Python 3.10 或更高版本
- Redis 服务器
- Docker（可选）

### 安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/zhangzhefang-github/websocket_project.git
   ```

2. 进入项目目录：

   ```bash
   cd websocket_project
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

### 运行服务器：

   ```bash
   python src/app.py
   ```

### 使用 Docker 运行

1. 启动服务：

   ```bash
   docker-compose --env-file .env.development up -d
   ```

2. 关闭服务：

   ```bash
   docker-compose --env-file .env.development down
   ```

### 配置

配置文件位于 [config.yaml](config.yaml)，可以根据需要进行修改，并支持实时更新。

### 贡献

欢迎贡献代码和改进建议。请参阅 [贡献指南](CONTRIBUTING.md) 了解更多信息。
