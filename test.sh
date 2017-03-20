#!/bin/sh

# set -m # Enable Job Control

# for i in `seq 10`; do # start 30 jobs in parallel
#   curl --data "writing to the file in thread $i" localhost:8080/files/test.txt &
# done


for i in `seq 4`; do # start 30 jobs in parallel
  chunk = '_1111111111222222222233333333334444444444555555555566666666667777777777888888888899999999990000000000_'
  curl localhost:8080/files/test.txt &
  curl --data "thread$i " localhost:8080/files/test.txt &
done

# Wait for all parallel jobs to finish
while [ 1 ]; do fg 2> /dev/null; [ $? == 1 ] && break; done
