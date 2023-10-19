#!/usr/bin/bash
echo "Installing requirements"
pip install -r requirements.txt
python main.py prod &
echo "sleep 5"
sleep 5
echo "finished waiting"
python test.py 
echo "done testing"
return 0