import requests

# Create a request object
# response = requests.post('http://127.0.0.1:5000/train', json={'input': {'x':[123,23],"y":[2,23],},"output":{"VL":[2,2]},})
response = requests.get('http://127.0.0.1:5000/train', json={'input': {"modelReference":"-2803657691561295276"},})

# Check the response status code
if response.status_code == 201:
  pass
else:
  print(response.text)
  # The request failed