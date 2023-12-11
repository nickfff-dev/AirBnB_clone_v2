#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

# Install Nginx if it is not already installed
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# Create the required directories if they do not exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "/server_name _;/a location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default

# Restart Nginx
sudo /etc/init.d/nginx restart
