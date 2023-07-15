from flask import Flask
from housing.logger import logging
from housing.exception import HousingException, sys

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    try:
        raise Exception("Testing custom exception")
    except Exception as e:
        housing = HousingException(e, sys)
        logging.info(housing.error_message)
        logging.info("testing the logging module")
    return "ci/cd pipeline established"


if __name__ == "__main__":
    app.run(debug=True)
