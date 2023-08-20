FROM mysql:5.7

ENV MYSQL_ROOT_PASSWORD=root_password
ENV MYSQL_DATABASE=fastapi
ENV MYSQL_USER=fastapi
ENV MYSQL_PASSWORD=fastapi

EXPOSE 3306
ADD ./mysql-init-files/ /docker-entrypoint-initdb.d/
