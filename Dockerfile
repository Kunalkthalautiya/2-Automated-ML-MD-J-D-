# Base Image
FROM python:3.8

# Working Directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run Flask App
CMD ["python", "app.py"]
