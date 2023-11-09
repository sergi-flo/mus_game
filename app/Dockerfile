# Use the official Python image as the base image
FROM python:3.9

# Copy your Python requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy your Python files into the container
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# Start your Flask app
CMD ["python", "app.py"]
