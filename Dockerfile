<<<<<<< HEAD
# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install project dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Django migrations
RUN python manage.py migrate

# Expose the port that the Django app will run on
=======
# Use the official Python image as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install project dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project files into the container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Django migrations
RUN python manage.py migrate

# Expose the port that the Django app will run on
>>>>>>> 9b032624ebbc1cb897feae06dd9936a2c25a05a6
EXPOSE…