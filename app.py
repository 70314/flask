from concurrent.futures import process
from multiprocessing.dummy import Process
from flask import Flask, request
import json
from face import *

# Setup flask server
app = Flask(__name__)

#port = 5000


# Setup url route which will calculate
# total sum of array.
@app.route('/attendence')

def attend():
	#data = request.get_json()
	# print(data)

	# Data variable contains the
	# data from the node server
	#ls = data['array']
	#result = sum(ls) # calculate the sum

	result = start()
	#print("here",result)

	# Return data in json format
	#return json.dumps({"result":result})

@app.route('/arraysum', methods = ['POST'])
def sum_of_array():
	data = request.get_json()
	print(data)

	# Data variable contains the
	# data from the node server
	ls = data['array']
	result = sum(ls) # calculate the sum

	# Return data in json format
	return json.dumps({"result":result})

if __name__ == "__main__":
	app.run()
