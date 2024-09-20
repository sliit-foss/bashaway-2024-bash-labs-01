# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy current directory contents to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
