# Makefile for LightRAG OpenAI Demo Docker image

# Image name
IMAGE_NAME = lightrag-demo

# Default query for demo
QUERY ?= "Who is Oliver Twist?"

.PHONY: build run clean help

# Default target
help:
	@echo "Available targets:"
	@echo "  build  - Build the Docker image"
	@echo "  run    - Run the Docker container (requires OPENAI_API_KEY)"
	@echo "  clean  - Remove the Docker image"
	@echo ""
	@echo "Usage examples:"
	@echo "  make build                   - Build the Docker image"
	@echo "  make run QUERY=\"Your query\"  - Run with a specific query"
	@echo "  make clean                   - Remove the Docker image"

# Build the Docker image
build:
	@echo "Building Docker image $(IMAGE_NAME)..."
	docker build -t $(IMAGE_NAME) -f ./Dockerfile ..

# Run the Docker container
run:
	@if [ -z "$(OPENAI_API_KEY)" ]; then \
		echo "Error: OPENAI_API_KEY environment variable is not set"; \
		echo "Usage: make run OPENAI_API_KEY=your-api-key [QUERY=\"Your query\"]"; \
		exit 1; \
	fi
	docker run -e OPENAI_API_KEY=$(OPENAI_API_KEY) -e LOG_LEVEL=WARNING $(IMAGE_NAME) -q "$(QUERY)" -m global 2>&1 | grep -v -E "INFO:|INFO -|Warning: 'wcwidth' library not found"

# Clean up
clean:
	@echo "Removing Docker image $(IMAGE_NAME)..."
	docker rmi $(IMAGE_NAME) || true
