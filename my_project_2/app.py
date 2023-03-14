from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import random, string
from flask_migrate import Migrate, migrate
import os
def randomword(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# initialize Flask application
app=Flask(__name__)
# enable debug mode
app.debug = True
#database URI
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///Games.db'
#upload folder path
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
# maximum file size to upload
app.config['MAX_CONTENT'] = 16*1024*1024
#Images allowed
ALLOWED_EXTENSIONS =['png','jpeg','jpg','gif']

#creat func that possible objects for the images:
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
db = SQLAlchemy(app)
class Games(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    Game_title= db.Column(db.String, unique=False ,nullable=False)
    description = db.Column(db.String, unique=False,nullable=False)
    age= db.Column(db.Integer,unique =False, nullable = False)
    price = db.Column(db.Integer,unique =False, nullable =False)
    online_play= db.Column(db.String(20),unique =False, nullable=False)
    multiplayer= db.Column(db.String(20), unique=False , nullable=False)
    filename = db.Column(db.String, unique =False ,nullable=True)
    def __repr__(self):
        return f"Title :{self.Game_title} , price:{self.price}"

class comment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    game_id=db.Column(db.Integer, unique=False, nullable=False)
    name= db.Column(db.String(20), unique=False, nullable=False)
    comment_text= db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.String(20), unique=False, nullable=True)
    def __repr__(self):
        return f"Name:{self.name}, Content:{self.comment_text} , rating:{self.rating}"

migrate= Migrate(app,db)

@app.route("/")
def home():
    game_data= Games.query.all()
    return render_template("index.html", game_data=game_data)
@app.route("/add_data")
def add_data():
    return render_template("add_profile.html")

@app.route("/add", methods=['POST','GET'])
def game_management():
    if request.method == "POST":
        Game_title = request.form.get("Game_title")
        description = request.form.get("description")
        age = request.form.get("age")
        price = request.form.get("price")
        online_play= request.form.get("online_play")
        multiplayer = request.form.get("multiplayer")
        file = request.files.get("filename")
        randomstring=randomword(10)
        if allowed_file(file.filename):
            file_split= file.filename.split(".")
            final_name = f"{file_split[0]}_{randomstring}.{file_split[1]}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],final_name))
        file_name=f"{file_split[0]}_{randomstring}.{file_split[1]}"
        game_row = Games(Game_title=Game_title,description=description,age=age,price=price,online_play=online_play, multiplayer=multiplayer ,filename=file_name)
        db.session.add(game_row)
        db.session.commit()
        return redirect("/")
@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for('static',filename='uploads/'+filename))


@app.route('/game_info/<game_id>')
def game_info(game_id):
    game_specific = Games.query.get(game_id)
    comment_specific = comment.query.filter(comment.game_id==game_id)
    return render_template("game.data.html", game_specific = game_specific , comment_specific=comment_specific)

@app.route("/add_review", methods=['POST','GET'])
def comment_management():
    if request.method == "POST":
        name = request.form.get("name")
        comment_text = request.form.get("comment_text")
        game_id = request.form.get("game_id")
        rating = request.form.get("rating")
        comment_row = comment(name=name, comment_text=comment_text, rating=rating, game_id=game_id)
        db.session.add(comment_row)
        db.session.commit()
        return redirect("/")


@app.route("/delete/<int:id>")
def erase(id):
    data = Games.query.get(id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}/{filename}")
    db.session.delete(data)
    comment_specific = comment.query.filter(comment.game_id == id)
    for co in comment_specific:
        db.session.delete(co)
    db.session.commit()
    return redirect("/")
@app.route("/Update_game/<int:id>", methods=["POST", "GET"])
def Update_game(id):
    if request.method == "POST":
        data = Games.query.get(id)
        Game_title = request.form.get("Game_title")
        description = request.form.get("description")
        age = request.form.get("age")
        price = request.form.get("price")
        online_play = request.form.get("online_play")
        multiplayer = request.form.get("multiplayer")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
        file_name = file.filename
        if request.form.get("Game_title"):
            data.Game_title = Game_title
        if request.form.get("description"):
            data.description = description
        if request.form.get("age"):
            data.age= age
        if request.form.get("price"):
            data.price = price
        if request.form.get("online_play"):
            data.online_play = online_play
        if request.form.get("multiplayer"):
            data.multiplayer = multiplayer
        if request.files.get("filename"):
            data.filename = file_name
        db.session.commit()
        return redirect(url_for('game_info', game_id=id))
    else:
        return render_template("Update_game.html")

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_value = request.form.get("search string")
        _search = "%{0}%".format(search_value)
        game_info_ = Games.query.filter(Games.Game_title.like(_search)).all()
        return render_template('game.data.html', game_info=game_info_, pageTitle=' World of PS: Most common games', legend="Search Results")
    else:
        return redirect("/")

@app.route("/", methods=["GET", "POST"])
def filter_data():
    if request.method == "POST":
        filter_value = request.form["filter_value"]
        _filter = "%{0}%".format(filter_value)
        filtered_info = Games.query.filter(Games.Game_title.like(_filter)).all()
        return render_template("game.data.html", game_info=filtered_info, pageTitle=' World of PS: Most common games', legend="Filtered Results")
    else:
        return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']


# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['myinput']
#     return text.upper()

if __name__ =="__main__":
    app.run()
