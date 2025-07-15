#! /bin/bash
for i in {5001..5004}; do
    iperf3 -s -p $i &
done
wait
