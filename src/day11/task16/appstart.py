#appstart.py

from flask import  Flask
app=Flask(__name__)
from flask_cors import  CORS
CORS(app)
from controller import  *

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
    # http://192.168.30.14:5000