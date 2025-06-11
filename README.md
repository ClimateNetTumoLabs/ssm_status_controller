# ssm_status_controller

This repository represents the remote devices internet/power status tracker, and ssm controller via MQTT.

It pings to website's url, if the device has internet in django admin panel it shows `online` and `Connect` button to connect to it via SSM, else it shows `offline`.

The `connection_status.service` service runs the python file of status sending.

The `ssm_controller.service` service runs the python file of MQTT and SSM communication.

It waits for `start-ssm` message to execute the command `sudo systemctl start amazon-ssm-agent` and start the ssm agent, and for `stop-ssm` to stop the agent, if any other messages are sent, nothing happens.

The topics are `control/managed_node_id` and `control/all` which affects on all devices.

---

The setup is on https://github.com/ClimateNetTumoLabs/ssm_status_controller/wiki/Installation-of-this-repository
