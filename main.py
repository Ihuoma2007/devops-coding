import json
import os
from urllib import response

from flask import Flask
from flask import request
app = Flask(__name__)

RESPONSE = os.environ["RESPONSE"]

@app.route('/status')
	def endpoint (status)
	return {"result": "success"}

def root():
	ret = {
		'response': response
	}

	return json.dumps(ret)

if __name__ == "__main__":
	app.run()
	
