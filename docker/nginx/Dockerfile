FROM nginx:latest
# Setting up time zone
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# Replication configuration
COPY conf/nginx.conf /etc/nginx/nginx.conf
