#!/bin/bash
mongo --eval "var ROOTPW='$ROOTPW'; var ADMINPW='$ADMINPW'; var USERNAME='$USERNAME'; var USERPW='$USERPW';" --shell  <<EOF
use admin;
db.auth('root', ROOTPW);
db.createUser({user:'admin',pwd:ADMINPW,roles:[{role:'userAdminAnyDatabase',db:'admin'}]});
db.createUser({user:USERNAME,pwd:USERPW,roles:[{role:'readWrite',db:'test'}]});
EOF
