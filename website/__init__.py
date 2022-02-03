from flask import Flask 

def create_app(): # function-
    app =Flask(__name__) #__name__ name of the file that runs
    app.config['SECRET_KEY']='jajjajaja dsakjdaskjjk' #encrypt the data related to our website

    return app