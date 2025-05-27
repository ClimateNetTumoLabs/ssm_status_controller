#!/bin/bash

cp ServiceFiles/ssm_controller.service /etc/systemd/system/
cp ServiceFiles/connection_status.service /etc/systemd/system/

python3 -m venv app/venv
source app/venv/bin/activate

# Install Python dependencies
pip install -r app/requirements.txt

sudo systemctl daemon-reload

# Enable and start services
sudo systemctl enable ssm_controller.service
sudo systemctl start ssm_controller.service

sudo systemctl enable connection_status.service
sudo systemctl start connection_status.service

echo "Installation completed successfully."