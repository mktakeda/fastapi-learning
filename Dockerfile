# -------------------
# Stage 1 - Builder
# -------------------
FROM python:3.12-slim AS builder

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install poetry poetry-plugin-export

# Export only production dependencies (no dev, no hashes)
RUN poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

# -------------------
# Stage 2 - Runtime
# -------------------
FROM python:3.12-slim AS runtime

# Security best practices
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/bin:$PATH"

# Create non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /code

# Copy and install dependencies
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir "gunicorn" "uvicorn[standard]"

# Copy app files
COPY --from=builder /app/src ./src
COPY --from=builder /app/data ./data
COPY --from=builder /app/entrypoint.sh ./entrypoint.sh

# Set ownership and permissions
RUN chmod +x entrypoint.sh && \
    mkdir -p /code/secrets && \
    chown -R appuser:appgroup /code

# Switch to non-root user
USER appuser

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
CMD ["gunicorn", "src.main:app", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:8000", "-w", "4", "--access-logfile", "-"]
