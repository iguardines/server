from flask import Flask
import os
 

app = Flask(__name__)

DEBUG = True

@app.errorhandler(404)
def not_found(error):
	return "Not Found"


@app.route('/test', methods=['GET'])
def index():
	value= os.environ['CLAVE']
	return {"mensaje":2, "valor":value

if __name__ == "__main__":
	app.run(port=5000, debug= DEBUG)
