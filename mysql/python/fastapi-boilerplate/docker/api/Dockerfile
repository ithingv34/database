# Stage 1: Build
FROM python:3.10.2-slim-buster as builder

# Set the working directory
WORKDIR /home

# Ignore 'Running pip as the root user...' warning
ENV PIP_ROOT_USER_ACTION=ignore

# Update pip
RUN pip install --upgrade pip

# Install poetry
ENV POETRY_VERSION=1.5.1
RUN pip install "poetry==$POETRY_VERSION"

# Copy application files
COPY . /home

# Build wheel
RUN poetry build --format wheel

# Stage 2: Production
FROM python:3.10.2-slim-buster as production

# Set the working directory
WORKDIR /home

# Install system dependencies
RUN apt-get update \
    && apt-get -y install netcat \
    && apt-get clean

# Expose port
EXPOSE 8000

# Copy the wheel from the build stage
COPY --from=builder /home/dist/*.whl ./

# Install package
RUN pip install *.whl

COPY docker/api/start.sh /home/docker/api/start.sh
RUN chmod +x /home/docker/api/start.sh

ENTRYPOINT /home/docker/api/start.sh