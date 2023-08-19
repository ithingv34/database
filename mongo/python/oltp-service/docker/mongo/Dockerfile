# pull official base image
FROM mongo:latest

# Set the local timezone to Asia/Seoul (Seoul Time)
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
