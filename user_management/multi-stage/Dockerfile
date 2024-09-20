# Stage 1: Build stage
FROM python:3.9-alpine AS builder

# Set environment variables for security and performance
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies and build tools
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && apk add --no-cache libffi-dev openssl-dev

# Set working directory
WORKDIR /app

# Copy only requirements.txt to leverage caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Stage 2: Final stage (runtime only)
FROM python:3.9-alpine

# Set environment variables again
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy dependencies and app files from the build stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app /app

# Expose port 5000
EXPOSE 5000

# Use a non-root user for security
RUN adduser -D flaskuser
USER flaskuser

# Run the Flask app
CMD ["python", "app.py"]
