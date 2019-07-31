FROM python:3-slim
# Setting up time zone
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Setting up workspace
RUN mkdir -p /home/web
WORKDIR /home/web
# Adding dependencies
ADD requirements.txt /home/web/requirements.txt
RUN pip3 install -i https://pypi.douban.com/simple/ -r requirements.txt

# Start the application with gunicorn
CMD gunicorn -w 4 -b 0.0.0.0:5000 run:application
