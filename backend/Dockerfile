# --- Stage 1: Build Stage ---
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies for psycopg2 (Postgres driver)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install via pip into a local folder
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# --- Stage 2: Final Runtime Stage ---
FROM python:3.11-slim

WORKDIR /app

# Only copy the installed libraries from the builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Ensure the local bin is in the PATH so we can run uvicorn
ENV PATH=/root/.local/bin:$PATH

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]