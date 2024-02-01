#!/usr/bin/env bash
#script that set the servers for deployment of we_static

if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Define the folders
folders=("/data" "/data/web_static" "/data/web_static/releases" "/data/web_static/shared" "/data/web_static/releases/test")

# Create necessary folders if they don't exist
for folder in "${folders[@]}"
do
    if [ ! -d "$folder" ]; then
        sudo mkdir -p "$folder"
    fi
done

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link, delete if already exists
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership to the current user and group recursively
sudo chown -R $USER:$USER /data/

# Update Nginx configuration
sudo sed -i '#/location /hbnb_static/ { s#alias .*#alias /data/web_static/current/; }#' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
