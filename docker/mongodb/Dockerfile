
FROM mongo:latest

# Setting up time zone
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


ENV WORKDIR /usr/local/work
ENV AUTO_RUN_DIR /docker-entrypoint-initdb.d
ENV INSTALL_MONGO_SHELL setup.sh

# Setting up a working directory
RUN mkdir -p $WORKDIR

# Initialization commands for replicating databases
COPY ./$INSTALL_MONGO_SHELL $AUTO_RUN_DIR/
RUN chmod +x $AUTO_RUN_DIR/$INSTALL_MONGO_SHELL
