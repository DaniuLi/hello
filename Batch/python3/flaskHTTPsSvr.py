from flask import Flask
app = Flask(__name__)
app.run('0.0.0.0', debug=True, port=5111, ssl_context='adhoc')