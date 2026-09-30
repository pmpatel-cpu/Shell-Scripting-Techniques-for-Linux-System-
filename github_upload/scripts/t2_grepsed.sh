#!/bin/bash
grep ",Critical," data.csv > /tmp/t2_out.txt
wc -l < /tmp/t2_out.txt
