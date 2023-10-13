# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Copy the current directory contents into the container at /app
COPY . /django_cpu_intensive

# Set the working directory in the container
WORKDIR /django_cpu_intensive

# Install FastAPI and Uvicorn for ASGI server
#RUN pip install Django
RUN pip install --no-cache -r /django_cpu_intensive/requirements.txt


# Expose the port on which the application will run
EXPOSE 8002

# Start the application using Uvicorn
CMD ["gunicorn", "django_cpu_intensive.wsgi", "-w", "2", "-b", "0.0.0.0:8002"]
