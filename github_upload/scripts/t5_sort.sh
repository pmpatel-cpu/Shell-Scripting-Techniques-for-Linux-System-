#!/bin/bash
tail -n +2 data.csv | sort -t',' -k15 -nr | head -10
