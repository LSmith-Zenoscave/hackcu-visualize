# Install Stackdriver logging agent
curl -sSO https://dl.google.com/cloudagents/install-logging-agent.sh
sudo bash install-logging-agent.sh

# Install or update needed software
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
apt-get update
apt-get install -yq git supervisor python3 python3-pip
apt-get install -yq  nodejs
pip3 install --upgrade pip virtualenv

# Account to own server process
useradd -m -d /home/pythonapp pythonapp

# Fetch source code
export HOME=/root
git clone https://github.com/LSmith-Zenoscave/hackcu-visualize.git /opt/app

# npm setup
npm -C /opt/app/visualization-frontend install
npm -C /opt/app/visualization-frontend run build

# Python environment setup
virtualenv -p python3 /opt/app/env
source /opt/app/env/bin/activate
/opt/app/env/bin/pip install -r /opt/app/requirements.txt

# Set ownership to newly created account
chown -R pythonapp:pythonapp /opt/app

# Put supervisor configuration in proper place
cp /opt/app/python-app.conf /etc/supervisor/conf.d/python-app.conf

# Start service via supervisorctl
supervisorctl reread
supervisorctl update