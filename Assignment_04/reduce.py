#!/usr/bin/env python

import sys

total = 0
count = 0

# Reducer function
for line in sys.stdin:
    # Split the input by tab delimiter
    num, num_count = line.strip().split('\t')
    try:
        num = float(num)
        num_count = int(num_count)
        # Update the total and count
        total += num * num_count
        count += num_count
    except ValueError:
        pass  # Ignore non-numeric values

# Calculate the average
if count > 0:
    average = total / count
    print("AVERAGE="+str(average))

