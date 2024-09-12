# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY ../../requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code to the working directory
COPY . .

# Expose the port on which the FastAPI app runs
EXPOSE 8000

# Run the FastAPI app
CMD ["python3", "main.py"]
