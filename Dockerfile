# Use an official Python runtime as a parent image
FROM python:3.11.6-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Run od.py when the container launches
CMD ["python", "main.py"]

