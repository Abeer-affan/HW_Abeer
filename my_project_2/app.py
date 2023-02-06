from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import os

app=Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///Games.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
app.config['MAX_CONTENT'] = 16*1024*1024
ALLOWED_EXTENSIONS =['png','jpeg','jpg','gif']

#creat func that possible objects for the images:
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS
db = SQLAlchemy(app)
class Games(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    Game_title = db.Column(db.String(50), unique=False ,nullable=False)
    description = db.Column(db.String, unique=False,nullable=False)
    age= db.Column(db.Integer,unique =False, nullable = False)
    price = db.Column(db.Integer,unique =False, nullable =False)
    # online= db.Column(db.string(20), unique =False, nullable=False)
    filename = db.Column(db.String(100), unique =False ,nullable=True)
    def __repr__(self):
        return f"Title :{self.Game_title} , Director:{self.price}"

class comment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    game_id=db.Column(db.Integer, unique=False, nullable=False)
    name= db.Column(db.String(20), unique=False, nullable=False)
    comment_text= db.Column(db.String, unique=False, nullable=False)
    def __repr__(self):
        return f"Name:{self.name}, Content:{self.comment_text}"

migrate= Migrate(app,db)
@app.route("/")
def home():
    game_data = Games.query.all()
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
        play_online = request.form.get("play_online")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
        file_name=file.filename
        game_row = Games(Game_title=Game_title,description=description,age=age,price=price,play_online=play_online, filename=file_name)
        db.session.add(game_row)
        db.session.commit()
        return redirect("/")
@app.route("/display/<filename>")
def display_image(filename):
    return redirect(url_for('static',filename='uploads/' + filename))
@app.route('/game_info/<movie_id>')
def game_info(game_id):
    game_specific = Games.query.get(movie_id)
    comment_specific = comment.query.filter(comment.game_id==game_id)
    return render_template("game.data.html", game_specific=game_specific , comment_specific=comment_specific)

@app.route("/add_review", methods=['POST','GET'])
def review_management():
    if request.method == "POST":
        name = request.form.get("name")
        comment_text = request.form.get("comment_text")
        game_id = request.form.get("game_id")
        comment_row = comment(name=name,comment_text=comment_text,game_id=game_id)
        db.session.add(comment_row)
        db.session.commit()
        return redirect("/")



if __name__ =="__main__":
    app.run()
