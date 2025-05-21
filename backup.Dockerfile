# Stage 1: Build Stage
FROM python:3.12-slim AS build-stage

# Set environment variables to avoid pycache and .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry

# Copy the project files
COPY pyproject.toml poetry.lock* /app/

# Install dependencies from Poetry
RUN poetry install --no-root --only main

# Stage 2: Final Stage (Production Setup)
FROM python:3.12-slim AS production-stage

# Set environment variables to avoid pycache and .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev

# Copy only the necessary files from the build stage
COPY --from=build-stage /app /app

# Copy the .env file into the container (adjust the path if needed)
COPY .env /app/.env

# Expose the port that FastAPI will run on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
