#!/bin/bash

# 測位が開始されるのに少し時間がかかるため1分待つ
sleep 1m
cd $HOME/evaluate-gps-qzss
PATH=/usr/local/bin:$PATH
$HOME/.local/bin/pipenv run python $HOME/evaluate-gps-qzss/logger.py >> $HOME/evaluate-gps-qzss/data/stdout.txt 2>&1