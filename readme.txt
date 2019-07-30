ANOIA

Name:
From Terry Pratchets “Discworld”’s pantheon of gods:

“Goddess of Things That Get Stuck in Drawers, a minor goddess on the Discworld. When someone rattles a drawer and cries "How can it close on the damned thing but not open with it? Who bought this? Do we ever use it?", even though the person might be genuinely irritated or even exasperated, it is as praise unto Anoia. Faithful Anoians (worshippers of Anoia) purposefully rattle their drawers and complain every day. Anoia also finds objects that roll under other objects and things stuck in sofa cushions, and is considering handling stuck zippers. She eats corkscrews.“

Intention of use:

Inventory database for hackspaces or makerspaces.


Technical details:

Intended technological stack:
python with flask
gunicorn
nginx

html5 + css + js with bootstrap


This is what has been done on the original dev system to create the environment:

sudo apt-get install docker-compose
sudo usermod -aG docker $USER        # allows non-sudo docker commands
cd projects/anoia
#dockerfile would be created here
#example app.py and requirements.txt created
docker build –tag=first .
docker run -p4000:80 first #demo run

