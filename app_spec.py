# Attempt App specification 

def before_serve(x):return None
def authenticate(x): return True
def post(x): return authenticate
def get(x): return authenticate

users = {
	"1": 100,
	"2":200,
	"4": 500, 
	"5":0
	}

Keys = {
	"34213":10,
	"fher3":1,
	"3434":20
}

Models = {
	"3433r": lambda x: x**2,
	"3434": lambda y : y-2
}

@before_serve
def rate_limit(user):
	""" Check if the user still have creates to make requests other than buying credits?
	or user checks. **Limit model executions or training
		1. Each user in db would have a count that get changed by various actions.
	"""
	if user in users:
		return True
	else:
		return False

def decreaseCredit(user, n):
	""" use users id and number of credits to operate on credits to
	1. decrease credits by n
	2. return new credits. {"remaining": 10, "valid": True or False}
	3. Turn Valid to Flase if credits go below 0 (meaning not funded)
	"""
	NewCredit = 0
	return NewCredit

@authenticate
@post("/credits/increase/")
def creditIncrease(user, key):
	""""
	3. Store credit keys/sorts that users can use to buy credits. 
				#If they post them to an endpoint, they get points".
	3. return new Balance
	"""
	creditUp = Keys.get(key, 0)
	users[user] += creditUp
	return users[user]



@authenticate
@get("/credits/status")
def creditCheck(user):
	""" return remaining number of calls to apis or minutes
	"""

	return 100


@get("/models/all")
def model_list(user):
	"""
	list all model references in json format
	"""
	decreaseCredit(user, 1)

	return []


# @rate_limit
@authenticate
@post("/train/data/")
def trainingData(user, data):
	"""
	data posted via json format, with input and output provided in json name.
	"""
	return "Model"

# @rate_limit
@authenticate
@get("/models/run/<modelId>/")
def executeRequest(user, data):
	"""
	execute the request and return values
	"""
	return "results"



