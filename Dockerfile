# Use Python 3.13 slim image for production
FROM python:3.13-slim as base

# Add labels for better maintainability
LABEL maintainer="Label" \
      description="Description" \
      version="0.0.0"

# Set environment variables for Python
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies and security updates in one layer
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Create non-root user early for better security
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set work directory and fix ownership
WORKDIR /app
RUN chown appuser:appuser /app

# Switch to non-root user for dependency installation
USER appuser

# Set UV environment variables for non-root user
ENV UV_CACHE_DIR=/tmp/uv-cache \
    UV_NO_CACHE=1

# Copy dependency files with proper ownership
COPY --chown=appuser:appuser pyproject.toml uv.lock ./

# Install dependencies as non-root user
RUN uv sync --frozen --no-install-project --no-dev

# Copy application code with proper ownership
COPY --chown=appuser:appuser app/ ./app/

# Expose port
EXPOSE 8500

# Health check with better error handling
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8500/health || exit 1

# Run the application
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8500"] 