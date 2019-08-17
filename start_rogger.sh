cd /home/pi/evaluate-gps-qzss
PATH=/usr/local/bin:$PATH
pipenv run python logger.py >> /home/pi/evaluate-gps-qzss/data/stdout.txt 2>&1