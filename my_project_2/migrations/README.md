 
# PROJECT2- PS WORLD OF GAMES
## Create by :Abeer-Affan :)

## `Features`
* Add a game with its name, description, age, price, online-playing, multiplayer and image of the game.
* Display all the games and each game's detailed information including reviews.
* Add a review for a specific game.
* alter a specific field in the game.

#### _Check steps_
manually check if added games appear in home page/if deleted game are removed including all the info
/if reviews and rating are updated .

## `Usage`
* Clone the repository
* Install the required dependencies using pip install -r requirements.txt
* Run the following command to initiate the database flask db init
* Run the following command to perform migrations flask db migrate
* Run the following command to upgrade the database flask db upgrade
* Run the following command to start the application flask run
* The application will be running at http://localhost:5000/


# `html files`
### _index_
#### _Features:_
a home page using HTML, CSS and Jinja. The page features a navigation bar with two links
### _add_profile_
In this page defined to add more games to database and publish in Home page .
### _game.data_
In this part defineded the information for each game according to the variable in database.
and all of the second pages are connecting to the home page .

## design my python code 

This code creates a Flask app and sets up a SQLAlchemy database to store game information.
It allows you to add, view and display game information along with adding comments and rating for each game.
The routes defined include:
•	"/": the home page displays all games stored in the database.
•	"/add_data": the add data page for adding new games.
•	"/add": handles adding new game information to the database.
•	"/display/<filename>": displays the image for the corresponding game.
•	"/game_info/<game_id>": displays information for a specific game and its associated comments.
•	"/add_review": handles adding a comment for a specific game to the database

## notes
* According to function allowed images are :.png, .jpeg, .jpg and .gif.
* 