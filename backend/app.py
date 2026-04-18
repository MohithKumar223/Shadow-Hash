from flask import Flask
from route import routes

app = Flask(__name__)

app.register_blueprint(routes)

@app.route("/")
def home():
    return "EV CRM Backend Running"

if __name__ == "__main__":
    app.run(debug=True)