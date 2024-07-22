# Dockerfile-mariadb

FROM mariadb:latest

COPY init.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD=rootpassword \
    MYSQL_DATABASE=flaskdb

EXPOSE 3306

