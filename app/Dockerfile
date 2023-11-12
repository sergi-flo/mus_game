# Use the official Python image as the base image
FROM python:3.9

# Copy your Python requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy your Python files into the container
COPY . .

# Start your Flask app
CMD ["python", "app.py"]
