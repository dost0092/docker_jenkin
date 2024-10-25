# Use the official Python image from the Docker Hub
FROM python:3.12.6

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Flask app code into the container
COPY . .

# Expose the port that the app runs on
EXPOSE 5000

# Set the environment variable to run the Flask app
ENV FLASK_APP=app.py

# Command to run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]
