# Dockerfile-mariadb

# Use the official MariaDB image from Docker Hub
FROM mariadb:latest

# Copy the SQL script to initialize the database
COPY init.sql /docker-entrypoint-initdb.d/

# Set the environment variables
ENV MYSQL_ROOT_PASSWORD=rootpassword \
    MYSQL_DATABASE=flaskdb \
    MYSQL_USER=flaskuser \
    MYSQL_PASSWORD=flaskpassword

# Expose the default MariaDB port
EXPOSE 3306

