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

WORKDIR /code

# Install runtime dependencies only
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN pip install "uvicorn[standard]"

# Copy only the necessary files and folders
COPY --from=builder /app/src ./src
COPY --from=builder /app/data ./data
COPY --from=builder /app/entrypoint.sh ./entrypoint.sh

RUN chmod +x entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
