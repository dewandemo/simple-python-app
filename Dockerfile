# Use a slim version as parent image
FROM python:3.8-slim as base

# Install system dependencies (if needed)
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m myuser
USER myuser

WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use a specific port for the application
EXPOSE 5000
ENV FLASK_RUN_HOST=0.0.0.0

# Run the tests
FROM base as test
CMD ["python", "tests.py"]

# Define the final stage
FROM base as final
CMD ["python", "app.py"]

