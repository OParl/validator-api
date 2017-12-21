from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from oparl_validator.core.validator import Validator

app = FlaskAPI(__name__)

@app.route('/', methods=['GET'])
def index():
    return []

if __name__ == '__main__':
    app.run(debug=True)
