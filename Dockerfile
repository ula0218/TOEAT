# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Install dependencies for Poetry and build tools
RUN apk add --no-cache \
    build-base \
    gcc \
    musl-dev \
    libffi-dev \
    # openssl-dev \
    # cargo \
    curl \
    mysql-dev \
    pkgconfig

# Copy the rest of the application code
COPY . /usr/src/app/

RUN pip install -r /usr/src/app/requirements.txt

# Expose the port the app runs on
EXPOSE 80

# Copy entrypoint script
COPY entrypoint.sh /usr/src/app/

# Make entrypoint script executable
RUN chmod +x /usr/src/app/entrypoint.sh

# Run the entrypoint script
CMD ["/usr/src/app/entrypoint.sh"]
# CMD ["sh"]