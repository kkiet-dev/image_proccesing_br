# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir opencv-python-headless

# Install tkinter for GUI functionality
RUN apt-get update \
    && apt-get install -y python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Command to run the Python script
CMD ["python", "main.py"]
