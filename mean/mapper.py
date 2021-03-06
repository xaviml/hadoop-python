#!/usr/bin/env python
import sys

d = {}
# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	# split the line into words
	features = line.strip().split(',')
	
	year = features[0]
	airport = features[16]
	delay = features[15]
	cancelled = features[21] == "1"
	
	
	
	if not cancelled:
		try:
			delay = float(delay)
		except ValueError:
			continue
		
		if (year, airport) not in d:
			d[(year, airport)] = [delay, 1]
		else:
			d[(year, airport)][0] += delay
			d[(year, airport)][1] += 1
# flush dict
for y, a in d:
	print "%s,%s\t%f\t%d" % (y, a, d[(y, a)][0], d[(y, a)][1])
	
	
