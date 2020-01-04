# ANOIA

### Name:
From Terry Pratchets “Discworld”’s pantheon of gods:

“Goddess of Things That Get Stuck in Drawers, a minor goddess on the Discworld. When someone rattles a drawer and cries "How can it close on the damned thing but not open with it? Who bought this? Do we ever use it?", even though the person might be genuinely irritated or even exasperated, it is as praise unto Anoia. Faithful Anoians (worshippers of Anoia) purposefully rattle their drawers and complain every day. Anoia also finds objects that roll under other objects and things stuck in sofa cushions, and is considering handling stuck zippers. She eats corkscrews.“

### Intention of use:

Inventory database for hackspaces or makerspaces.


## Technical details:

### Intended technological stack:
python with flask
gunicorn
nginx

html5 + css + js with bootstrap

### Architecture:
```
anaoja # main project folder
\
 docker # holds the docker-compose config
 \
  flask     # holds docker file and enviroment definition (+template)
  |
  mongodb   # holds docker file, enviroment definition (+template) and setup script
  \
   db       # holds the actual db
  |
  nginx     # holds docker file
  \
   conf     # holds the nginx configuration
   |
   log      # holds the nginx log files
 |
 src	    # holds the flask app start file (+ local debug start)
 \
  app       # holds the rest of the source files
  \
   templates  # holds the html tenplate files for flask
   |
   static
   \
    assets  # unsorted java script files
    \
     css    # css files
     images # image files
     js     # javascript files
```

### This is what has been done on the original dev system to create the environment:
```bash
sudo apt-get install docker-compose
sudo usermod -aG docker $USER        # allows non-sudo docker commands
cd projects/anoia
#dockerfile would be created here
#example app.py and requirements.txt created
docker build –tag=first .
docker run -p4000:80 first #demo run
```

### How to start on the dev system:
```bash
cd anoja/docker
docker-compose up
#in another terminal:
firefox "http://localhost:8080/list"
```
