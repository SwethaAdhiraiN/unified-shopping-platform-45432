# Base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Install dependencies (requirements.txt will be added in subsequent steps as needed)
COPY . /app

# Install pip requirements if file exists
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Expose a default port (adjust as backend implementation dictates; often 8000 for Django)
EXPOSE 8000

# ENTRYPOINT or CMD (dummy command for now, to be replaced with real manage.py runserver or similar when code exists)
CMD [ "bash", "-c", "echo 'Django backend container is set up but no application code present.'" ]
