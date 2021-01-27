from flask import Flask
import yfinance as yf

app = Flask(__name__)

DEBUG = True
PORT = 5000

def __returnGMEdata__():
    return yf.download("gme").to_json()



@app.errorhandler(404)
def not_found(error):
	return "Not Found"


@app.route('/gme_historic', methods=['GET'])
def index():
	return __returnGMEdata__()


if __name__ == "__main__":
	app.run(port=5000, debug= DEBUG)
