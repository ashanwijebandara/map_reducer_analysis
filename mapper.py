#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
next(reader)  # skip header

for row in reader:
    if len(row) > 8:
        country = row[8]  
        print(f"{country}\t1")
