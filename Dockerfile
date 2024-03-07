# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables
# Note: These values will be passed during the container run
ENV MLFLOW_TRACKING_URI="https://mlflow.org" \
    HARNESS_PIPELINE_ID="12345678"

# Run app.py when the container launches
CMD ["python", "app.py"]
