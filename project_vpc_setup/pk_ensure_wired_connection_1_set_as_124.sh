#!/bin/bash

# set profile connection up for preventing unconnectable problem
# sudo nmcli connection modify "Wired connection 2" connection.interface-name "Wired connection 1"


# set IPv4 profile
sudo nmcli connection modify "Wired connection 1" ipv4.address "192.168.2.124/22"
sudo nmcli connection modify "Wired connection 1" ipv4.method manual
sudo nmcli connection modify "Wired connection 1" ipv4.gateway "192.168.1.1"
sudo nmcli connection modify "Wired connection 1" ipv4.dns "8.8.8.8"

# check profile again
sudo nmcli connection show "Wired connection 1" | grep ipv4.address
sudo nmcli connection show "Wired connection 1" | grep ipv4.method
sudo nmcli connection show "Wired connection 1" | grep ipv4.gateway
sudo nmcli connection show "Wired connection 1" | grep ipv4.dns


# set profile connection down and up 
sudo nmcli connection down "eth1"
sudo nmcli connection down "eth0"
sudo nmcli connection down "Wired connection 1"
sudo nmcli connection up "Wired connection 1"

ping -c 3 8.8.8.8
