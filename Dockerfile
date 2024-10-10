FROM python:3.12-slim

# 更新并安装必要的工具
RUN apt-get update && \
    apt-get install -y inetutils-telnet redis-tools && \
    rm -rf /var/lib/apt/lists/*  # 清理缓存，减小镜像大小

# 设置工作目录
WORKDIR /app

# 复制需求文件并安装依赖
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 指定容器启动时执行的命令
CMD ["python", "src/app.py"]
