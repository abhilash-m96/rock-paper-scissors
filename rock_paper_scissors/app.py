from flask import Flask
from flask_restful import Api
import os

from resources.rock_paper_scissors import Game

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rock_papers_scissors.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = os.environ["SECRET_KEY"]
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Game, "/rockPaperScissors/<string:user_input>")

if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
