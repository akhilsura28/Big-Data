#!/usr/bin/env python

import sys

my_dict = {}

for line in sys.stdin:
        # Split the line into words
    values = line.strip().split()
    for value in values:
        try:
            # Convert the value to a float
            num = float(value)
            if num in my_dict:
                 my_dict[num] += 1
            else:
                 my_dict[num] = 1 
            # Emit the value with a count of 1
            #print '%d\t%d' % (num, 1)                                     
        except ValueError:
                continue
                # Ignore non-numeric values

for number, count in my_dict.items():
     print '%d\t%d' % (number, count) 