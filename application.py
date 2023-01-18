from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_from_nazim():
    return "<b><font color=blue>Hello GitHub Actions World from Nazim Huseynov!</font></b>"

@application.route('/aboutme')
def aboutme():
    return "<b><font color=green>My name is Nazim. I am a Cloud/DevOps Engineer!</font></b>"

if __name__ == "__main__":
    application.run()