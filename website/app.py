from flask import Flask, render_template

#init app
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#run server
if __name__ =="__main__":
    app.run(debug=True)