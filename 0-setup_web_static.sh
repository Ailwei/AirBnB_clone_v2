#!/usr/bin/env bash
#script that set the servers for deployment of we_static
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create necesasry directions for web_static
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/test/index.html

# create the html link 
sudo echo "<html>
  <head>
  </head>
  <body>
   Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbtn_static { alias /data/web_static/current/:}' /etc/nginx/sites-enabled/default

sudo service nginx restart
