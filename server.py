import json
import uuid

from flask import Flask, jsonify, abort
from flask_cors import CORS

from database import save_game_state, get_last_game_state
from catanatron.game import Game
from catanatron.json import GameEncoder
from catanatron.models.player import RandomPlayer, Color
from catanatron.players.greedy_estimate import GreedyEstimatePlayer


app = Flask(__name__)
CORS(app)


@app.route("/games", methods=["POST"])
def create_game():
    game = Game(
        players=[
            GreedyEstimatePlayer(Color.RED),
            RandomPlayer(Color.BLUE),
            RandomPlayer(Color.WHITE),
            RandomPlayer(Color.ORANGE),
        ]
    )
    save_game_state(game)
    return jsonify({"game_id": game.id})


@app.route("/games/<string:game_id>", methods=["GET"])
def get_game_endpoint(game_id):
    game = get_last_game_state(game_id)
    if game is None:
        abort(404, description="Resource not found")

    return json.dumps(game, cls=GameEncoder)


@app.route("/games/<string:game_id>/tick", methods=["POST"])
def tick_game(game_id):
    game = get_last_game_state(game_id)
    if game is None:
        abort(404, description="Resource not found")

    if game.winning_player() is None:
        game.play_tick(lambda g: save_game_state(g))
    return json.dumps(game, cls=GameEncoder)
