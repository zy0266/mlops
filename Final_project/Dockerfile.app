# Use a lightweight version of Python as base image
FROM python:3.9.16-slim

# Set the working directory inside the container
WORKDIR /app_home

# Copy the local application code to the container
COPY ./web_service /app

# Navigate to the application directory
WORKDIR /app

# Install required dependencies
COPY requirements_app.txt .
RUN pip install --no-cache-dir -r requirements_app.txt

# Expose port 8045 to allow communication
EXPOSE 8000

# Start FastAPI app with Uvicorn (set host to 0.0.0.0 to allow access from outside the container)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


