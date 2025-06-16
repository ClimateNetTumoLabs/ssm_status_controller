# Remote Device Status Tracker & SSM Controller via MQTT
This repository provides a solution for monitoring the internet and power status of remote devices, and controlling them via AWS Systems Manager (SSM) through MQTT communication.

## Overview
Devices periodically ping a specified website URL.

If a device has internet access, its status is shown as Online in the Django admin panel, along with a Connect button to initiate an SSM session.

If no internet access is detected, the device is marked as Offline.

## Services
Two systemd services are responsible for the functionality:

`connection_status.service`
Runs a Python script that sends the current internet/power status of the device.

`ssm_controller.service`
Runs a Python script that listens for MQTT messages and controls the AWS SSM agent accordingly.

## MQTT Control
The MQTT controller listens for the following messages:

start-ssm → Executes:

```bash
sudo systemctl start amazon-ssm-agent
```
Starts the SSM agent on the device.

stop-ssm → Executes:

```bash
sudo systemctl stop amazon-ssm-agent
```
Stops the SSM agent unless a new start request is received.

Any other messages are ignored.

## Topics
MQTT topics used:

`control/<managed_node_id>` – Targets a specific device.

`control/all` – Broadcasts to all connected devices.

## Manual Message Sending
In addition to the Django admin interface, MQTT messages can also be sent manually using the AWS IoT Core MQTT Test Client.

## Setup
Setup instructions are available in the [Wiki](https://github.com/ClimateNetTumoLabs/ssm_status_controller/wiki/Installation-of-this-repository).
