#!/usr/bin/bash
echo "Installing requirements"
pip install -r requirements.txt
python main.py prod &
echo "wait 15"
wait 15
echo "finished waiting"
python test.py
echo "done testing"
return 0