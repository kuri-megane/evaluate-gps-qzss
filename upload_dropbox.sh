#!/bin/bash

sleep 3m 
TODAY=$(date "+%Y%m%d")
zip $HOME/log-$TODAY-pi.zip $HOME/evaluate-gps-qzss/data/*
$HOME/Dropbox-Uploader/dropbox_uploader.sh upload $HOME/log-$TODAY-pi.zip .
rm $HOME/log-$TODAY-pi.zip