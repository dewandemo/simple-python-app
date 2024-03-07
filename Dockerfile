# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define a build argument
ARG HARNESS_PIPELINE_ID
ARG MLFLOW_TRACKING_URI

# Define a env var

ENV HARNESS_PIPELINE_ID=${HARNESS_PIPELINE_ID}
ENV MLFLOW_TRACKING_URI=${MLFLOW_TRACKING_URI}

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
