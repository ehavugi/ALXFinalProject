#!/usr/bin/bash
pip install -r requirements.txt
python main.py &
echo "wait 5"
wait 5
python test.py