import random
from flask_restful import Resource
from models.game_data import GameLog


class Game(Resource):
    POSSIBLE_ACTIONS = ["rock", "paper", "scissors"]
    USER_WIN_STATEMENT = "User wins!"
    BOT_WIN_STATEMENT = "Bot wins!"

    def get(self, user_input: str):
        if user_input not in self.POSSIBLE_ACTIONS:
            return {"message": "Invalid choice", "choices": self.POSSIBLE_ACTIONS}

        self.user_input = user_input
        self.bot_input = self.generate_bot_input()
        self.result = self.calculate_result()

        game_log = GameLog(self.user_input, self.bot_input, self.result)
        game_log.save_to_db()

        return {
            "data": {
                "your_input": self.user_input,
                "bot_input": self.bot_input,
                "outcome": self.result,
            }
        }

    def generate_bot_input(self):
        bot_input = random.choice(self.POSSIBLE_ACTIONS)
        return bot_input

    def calculate_result(self):
        if self.user_input == self.bot_input:
            return "Tie"
        elif self.user_input == "rock":
            if self.bot_input == "scissors":
                return self.USER_WIN_STATEMENT
            else:
                return self.BOT_WIN_STATEMENT
        elif self.user_input == "paper":
            if self.bot_input == "rock":
                return self.USER_WIN_STATEMENT
            else:
                return self.BOT_WIN_STATEMENT
        elif self.user_input == "scissors":
            if self.bot_input == "paper":
                return self.USER_WIN_STATEMENT
            else:
                return self.BOT_WIN_STATEMENT
