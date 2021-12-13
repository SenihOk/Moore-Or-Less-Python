from flask import Flask
import addadvice
app = Flask(__name__)

@app.route('/')

def index():
    return addadvice.Advice('this is a test. ').addAdvice()

app.run()
    
 