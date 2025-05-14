# Build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Install additional dependencies needed for the demo
RUN pip install --user --no-cache-dir tabulate openai tiktoken networkx graspologic nano-vectordb

# Final stage
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy LightRAG library code
COPY ./lightrag ./lightrag
COPY setup.py .

# Copy the demo script
COPY ./examples/lightrag_openai_demo_query_only.py ./examples/

# Copy Dickens dataset files
COPY ./dickens/ ./dickens/
COPY ./examples/dickens/ ./dickens/

# Set environment variables
ENV PYTHONPATH=/app
ENV OPENAI_API_KEY=""

# Set entrypoint
ENTRYPOINT ["python", "examples/lightrag_openai_demo_query_only.py"]
