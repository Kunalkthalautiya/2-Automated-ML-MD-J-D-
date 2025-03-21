# Base Image
FROM python:3.8

# Working Directory
WORKDIR /app

# Copy files
COPY requirements.txt requirements.txt
COPY train_model.py train_model.py
COPY model.pkl model.pkl
COPY app.py app.py

# Install dependencies
RUN pip install -r requirements.txt

# Run Flask App
CMD ["python", "app.py"]
