from db import db


class GameLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(20), nullable=False)
    bot_input = db.Column(db.String(20), nullable=False)
    result = db.Column(db.String(20), nullable=False)

    def __init__(self, user_input, bot_input, result):
        self.user_input = user_input
        self.bot_input = bot_input
        self.result = result

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # THIS WILL BE USED BY ENDPOINT WHICH IS YET TO BE IMPLEMENTED
    def json(self):
        return {
            "id": self.id,
            "your_input": self.user_input,
            "bot_input": self.bot_input,
            "result": self.result,
        }
