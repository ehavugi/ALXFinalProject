import requests

# Create a request object
# response = requests.post('http://127.0.0.1:5000/train', json={'input': {'x':[16,15,14],"y":[2,5,10],},"output":{"VL":[12,55,100]},})
# response = requests.get('http://127.0.0.1:5000/train', json={'input': {"modelReference":"-2803657691561295276"},})
# response = requests.get('http://127.0.0.1:5000/train', json={'input': {'x':[13,35,23],"y":[6,23,35],"modelReference":"-2587665098986755032"}})
# response = requests.get('http://127.0.0.1:5000/train', json={'input': {'x':[6,5,1 ],"y":[2,5,20],"modelReference":"-2587665098986755032"}})
response = requests.get('http://127.0.0.1:5000/train', json={'input': {'x':[16,15,14 ],"y":[2,5,10],"modelReference":"-2469777098239407370"}})

print(response.request)
# Check the response status code
if response.status_code == 201:
  pass
else:
  print(response.text)
  # The request failed


# {
#   "coeff": [
#     [
#       6.879999999999999,
#       5.1599999999999975
#     ]
#   ],
#   "input_shape": [
#     2,
#     2
#   ],
#   "intercept": [
#     -5.199999999999989
#   ],
#   "modelReference": -4577614554448436428,
#   "output_shape": [
#     2,
#     1
#   ],
#   "score": "1.0",
#   "time": 1694907978.396081,
#   "trained": true
# }

# [Finished in 3.0s]


# curl -d '{"input":{"x":[13,35,23],"y":[6,23,35],"modelReference":"1157746954101703716"}}' -H "Content-Type: application/json" -X GET http://localhost:5000/train
# curl --json '{"input":{"x":[6,5],"y":[2,5]},"output":{"VL":[12,55]}}' -X POST http://localhost:5000/train