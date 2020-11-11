# catanatron

[![Coverage Status](https://coveralls.io/repos/github/bcollazo/catanatron/badge.svg?branch=master)](https://coveralls.io/github/bcollazo/catanatron?branch=master)

Settlers of Catan simluation environment in Python and Machine-Learning player.

## Usage

You can create your own AI bots/players implementing the following API:

```python
from catanatron.models.players import Player

class MyPlayer(Player):
    def decide(self, game: Game, playable_actions: Iterable[Action]):
        """Should return one of the playable_actions.

        Args:
            game (Game): complete game state. read-only.
            playable_actions (Iterable[Action]): options right now
        """
        raise NotImplementedError
```

## Running and Watching a Game

To visualize a game execution, you'll need to run 3 components. A React UI, a Flask
Web Server, and a PostgreSQL database (provided in docker container). Run the
following on three different Terminal tabs.

### React UI

Make sure you have `yarn` installed (https://classic.yarnpkg.com/en/docs/install/).

```
cd ui/
yarn install
yarn start
```

### Flask Web Server

Make sure you have `pipenv` installed (https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv).

```
pipenv install
pipenv shell
export FLASK_ENV=development
export FLASK_APP=server.py
flask run
```

### PostgreSQL Database

Make sure you have `docker-compose` installed (https://docs.docker.com/compose/install/).

```
docker-compose up
```

### Running a Game

After bringing up the three components, you can run the `play.py` script which
will run a game and print out a link to watch the game.

```
python play.py
```

## Developing for Catanatron

To develop for Catanatron core logic you can use the following test suite:

```
coverage run --source=catanatron -m pytest tests/ && coverage report
```

Or you can run the suite in watch-mode with:

```
ptw --ignore=tests/integration_tests/ --nobeep
```

## Machine Learning

To play games and save to database (for experience):

```
python play.py --num=100
```

To use these games from database and train a value-estimating model:

```
python create_feature_matrix.py
```

## For Testing Performance:

```
python -m cProfile play.py --num=5 -o profile.pstats
snakeviz profile.pstats
```
