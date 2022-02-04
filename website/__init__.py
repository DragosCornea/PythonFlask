from flask import Flask 

#init app
app= Flask(__name__)

@app.route('/')
def index():
    return "Hello"

#run server
if __name__ =="__main__":
    app.run(debug=True)
    