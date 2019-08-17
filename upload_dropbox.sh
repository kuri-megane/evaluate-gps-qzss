#!/bin/bash
 
## config
TODAY=$(date "+%Y%m%d")

## web backup
zip $HOME/log-$TODAY-pi.zip $HOME/evaluate-gps-qzss/data/*
## backup to dropbox
$HOME/Dropbox-Uploader/dropbox_uploader.sh upload $HOME/log-$TODAY-pi.zip .
rm $HOME/log-$TODAY-pi.zip