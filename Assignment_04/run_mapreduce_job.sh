#!/bin/bash
/usr/bin/hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-files map.py,reduce.py \
-input /mapreduce/average_num/avg.txt \
-output /mapreduce/average_num/output02 \
-mapper map.py \
-reducer reduce.py 

