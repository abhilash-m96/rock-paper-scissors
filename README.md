# rock-paper-scissors
Rock paper scissors API

The API uses 'GET' method keeping in mind it can be tested in browser and it does not
require tools like POSTMAN 

## ENDPOINT:
http://hostname:5000/rockPaperScissors/input


## Valid Endpoint choices:

http://hostname:5000/rockPaperScissors/rock
http://hostname:5000/rockPaperScissors/paper
http://hostname:5000/rockPaperScissors/scissors

## INSTALLATION
Run the below command
```
pip3 install -r requirements.txt
```

Export an environment variable
```
export SECRET_KEY="secret_key"
```

To start the service
```
python3 app.py
```
## Explore db
All the data will be stored in an auto created db `rock_paper_scissors.db`
this can be explored by running the command `sqlite3 rock_paper_scissors.db`
