#!/bin/bash

# Server IP address (replace with your server's IP address)
SERVER_IP="192.168.2.123"

# UDP datagram size in bytes
DATAGRAM_SIZE=65000

# Duration of the test in seconds  
# 86400 seconds == 24 hours
DURATION=86400


# UDP test function
# This function starts an iperf3 client that sends UDP packets to the server
start_client() {
    echo $1
    iperf3 -c $SERVER_IP -p $1 -u -b 100M -l $DATAGRAM_SIZE -t $DURATION
}

# Start 4 iperf3 clients in parallel
for i in {5001..5004}; do
    start_client $i &
done

# Wait for all background processes to finish
wait