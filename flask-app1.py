from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_from_nazim():
    return 'Hello GitHub Actions World from Nazim Huseynov!'

@application.route('/aboutme')
def aboutme():
    return 'I am a Cloud/DevOps Engineer'

if __name__ == "__main__":
    application.run()