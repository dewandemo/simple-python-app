# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy the Python script to the container
COPY app.py .

# Create a directory for output and set permissions
RUN mkdir /output && chmod 777 /output

# Run the Python script
CMD ["python", "app.py"]
