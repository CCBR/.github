# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Update the package list and install bash
RUN apt-get update && \
    apt-get install -y bash && \
    apt-get clean

# Install the required Python packages
RUN pip install --no-cache-dir pandas requests python-dateutil tabulate