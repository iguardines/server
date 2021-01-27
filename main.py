from flask import Flask

app = Flask(__name__)

DEBUG = True

@app.errorhandler(404)
def not_found(error):
	return "Not Found"


@app.route('/test', methods=['GET'])
def index():
	return {"mensaje":2}


if __name__ == "__main__":
	app.run(port=5000, debug= DEBUG)
