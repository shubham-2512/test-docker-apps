# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Copy the current directory contents into the container at /app
COPY . /cpu_intensive

# Set the working directory in the container
WORKDIR /cpu_intensive

# Install FastAPI and Uvicorn for ASGI server
RUN pip install fastapi uvicorn

# Expose the port on which the application will run
EXPOSE 8002

# Start the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]