# Use the official Python image from the Docker Hub
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install Flask-Migrate
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]


#CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "flaskapp:app"]

