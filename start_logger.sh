#!/bin/bash

sleep 1m
cd $HOME/evaluate-gps-qzss
PATH=/usr/local/bin:$PATH
$HOME/.local/bin/pipenv run python logger.py >> /home/pi/evaluate-gps-qzss/data/stdout.txt 2>&1