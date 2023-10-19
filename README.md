# ALXFinalProject

Technology uses
* web technologies 
	 + Flask
* Application technologies
	 + Sklearn

* database**
	 + sqlite db


## Key App feature
1. Authentication
2. Rate limited / account management
3. ML server


## API support
+ POST /register , method POST, json = {username:username, password:pwd}
+ POST /login, method POST, json= {username:username, password:pwd}
+ POST /train, json = { 'input': {'x': [16, 15, 14], "y": [2, 5, 10]},     'output': {"VL": [12, 55, 100]}}
+ GET models/all , GET 
+ GET /credits/status, GET
+ GET /models/all
+ GET /credits/status 
+ GET /models/all 
+ GET /credits/status 
+ GET /test