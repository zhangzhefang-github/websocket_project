<p align="center">
    <br> <a href="README-EN.md">English</a> | 中文
</p>

- [WebSocket 服务器项目](#websocket-服务器项目)
  - [特性](#特性)
  - [产品截图](#产品截图)
  - [快速开始](#快速开始)
    - [先决条件](#先决条件)
    - [安装](#安装)
    - [运行服务器](#运行服务器)
    - [使用 Docker 运行](#使用-docker-运行)
    - [配置](#配置)
  - [贡献](#贡献)
  - [许可证](#许可证)
  - [联系](#联系)
  - [项目链接](#项目链接)

# WebSocket 服务器项目

这是一个高性能的 WebSocket 服务器项目，具备高可扩展性、高可用性和国际化支持。该项目基于实时更新，确保服务的稳定性和高效性。

## 特性

- **高扩展性**：模块化设计，方便功能扩展和维护，支持实时更新。
- **高可用性**：优化的连接管理和错误日志记录，保证服务的稳定性和实时更新。
- **性能监控**：集成 Prometheus，提供关键指标的实时监控和更新。
- **Redis 支持**：使用异步 Redis 客户端，高效获取数据，并支持实时更新。
- **配置灵活**：支持环境变量和配置文件，方便部署和配置，并支持实时更新。

## 产品截图

![产品截图](./docs/screenshot.png)

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

### 运行服务器

   ```bash
   python src/app.py
   ```

### 使用 Docker 运行

1. 拉取镜像文件：

   ```bash
   docker pull zhangzhefang/websocket-server
   ```

2. 启动服务：

   ```bash
   docker-compose --env-file .env.development up -d
   ```

3. 关闭服务：

   ```bash
   docker-compose --env-file .env.development down
   ```

### 配置

配置文件位于 [config.yaml](config.yaml)，可以根据需要进行修改，并支持实时更新。

## 贡献

欢迎贡献代码和改进建议。请参阅 [贡献指南](CONTRIBUTING.md) 了解更多信息。

## 许可证

该项目根据 Apache-2.0 许可证的条款进行许可。详情请参见 [LICENSE](LICENSE) 文件。

## 联系

如有任何问题或建议，请联系 zhangzhefang@msn.cn。

## 项目链接

项目的 GitHub 仓库链接为: [WebSocket 服务器项目](https://github.com/zhangzhefang-github/websocket_project)
