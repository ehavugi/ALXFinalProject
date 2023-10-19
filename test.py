"""
Create User, persist sesion across multiple user interaction

Todo:
  1. High data calls. Large inputs
  3. Use a previosuly created model id
  4.  
"""
import requests
import json

# Create a session to persist cookies
session = requests.Session()

# Define the base URL 
base_url = "http://localhost:8080"

# Registration and login payload
payload = {
    'username': '1',
    'password': 'password1'
}

# Register the user
register_url = f"{base_url}/register"
response = session.post(register_url, json=payload)
print(response.text)

# Log in the user
login_url = f"{base_url}/login"
response = session.post(login_url, json=payload)
print(response.text)

# Make  subsequents request using the session
model_training_payload = {
    'input': {'x': [16, 15, 14], "y": [2, 5, 10]},
    'output': {"VL": [12, 55, 100]}
}
train_url = f"{base_url}/train"
response = session.post(train_url, json=model_training_payload)

print(response.text)

response = session.get(f"{base_url}/models/all")

print(response.text)

response = session.get(f"{base_url}/credits/status")
print(response.text)

response = session.get(f"{base_url}/models/all")

print(response.text)

response = session.get(f"{base_url}/credits/status")
print(response.text)


response = session.get(f"{base_url}/models/all")

print(response.text)

response = session.get(f"{base_url}/credits/status")
print(response.text)

response = session.get(f"{base_url}/models/all")

print(response.text)

response = session.get(f"{base_url}/credits/status")
print(response.text)
response = session.get(f"{base_url}/models/all")

print(response.text)

response = session.get(f"{base_url}/credits/status")
print(response.text)


# more  requests using the same session for demo?
# For example, making an API call
api_call_url = f"{base_url}/api_call"
response = session.get(api_call_url)
print(response.text)

response = session.get(f'{base_url}/test', json={'input': {'x':[16,15,14 ],"y":[2,5,10],"modelReference":"-2469777098239407370"}})

print(response.request)
# Check the response status code
if response.status_code == 201:
  pass
else:
  print(response.text)
