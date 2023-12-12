# This manifest sets up web servers for deployment of web_static

# Install Nginx if it is not already installed
exec { 'apt-update':
  command  => '/usr/bin/apt-get update',
  provider => shell,
}

exec { 'install-nginx':
  command  => '/usr/bin/apt-get install -y nginx',
  provider => shell,
  require  => Exec['apt-update'],
}

# Create the required directories if they do not exist
exec { 'create-directories':
  command  => '/bin/mkdir -p /data/web_static/releases/test/ /data/web_static/shared/',
  provider => shell,
}

# Create a fake HTML file
exec { 'create-html':
  command  => '/bin/echo "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" | sudo tee /data/web_static/releases/test/index.html',
  provider => shell,
  require  => Exec['create-directories'],
}

# Create a symbolic link
exec { 'create-symlink':
  command  => '/bin/ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => shell,
  require  => Exec['create-html'],
}

# Give ownership of the /data/ folder to the ubuntu user AND group
exec { 'change-ownership':
  command  => '/bin/chown -R ubuntu:ubuntu /data/',
  provider => shell,
  require  => Exec['create-symlink'],
}

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
exec { 'update-nginx-config':
  command  => '/bin/sed -i "/server_name _;/a location /hbnb_static/ {\\n\\t\\talias /data/web_static/current/;\\n\\t}" /etc/nginx/sites-available/default',
  provider => shell,
  require  => Exec['install-nginx'],
}

# Restart Nginx
exec { 'restart-nginx':
  command  => '/etc/init.d/nginx restart',
  provider => shell,
  require  => Exec['update-nginx-config'],
}
