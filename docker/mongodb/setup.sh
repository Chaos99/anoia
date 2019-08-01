#!/bin/bash
mongo <<EOF
use admin;
db.auth('root', '123456');
db.createUser({user:'admin',pwd:'admin',roles:[{role:'userAdminAnyDatabase',db:'admin'}]});
db.createUser({user:'test',pwd:'test',roles:[{role:'readWrite',db:'test'}]});
db.createCollection("user");
EOF
