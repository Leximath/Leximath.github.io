#!/bin/bash
./pares_fino.sh > fino.csv 
./pares_grosso.sh > grosso.csv
python2.7 convert2nested.py grosso.csv processo flare.json 0 1 2 fino.csv
