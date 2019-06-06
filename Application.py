from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from models.Sex import Sex
from models.Species import Species
from models.SpeciesOfSharks import SpeciesOfSharks
from models.SwimType import SwimType

from Main import main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:adminYura@localhost:3306/zoo_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class SharkModel(db.Model):
    __tablename__ = 'sharks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(length=100))
    age = db.Column(db.Integer)
    year_in_zoo = db.Column(db.Integer)
    sex = db.Column(db.String(length=6))
    volume_of_aquarium = db.Column(db.Integer)
    species = db.Column(db.String(length=20))
    species_of_sharks = db.Column(db.String(length=30))
    speed = db.Column(db.Integer)
    swim_type = db.Column(db.String(length=20))

    def __init__(self, name="", age=0, year_in_zoo=0, sex=None, volume_of_aquarium=0, species=None, species_of_sharks=None, speed=0, swim_type=None):
        self.name = name
        self.age = age
        self.year_in_zoo = year_in_zoo
        self.sex = str(sex)
        self.volume_of_aquarium = volume_of_aquarium
        self.species = str(species)
        self.species_of_sharks = str(species_of_sharks)
        self.speed = speed
        self.swim_type = str(swim_type)

    def __str__(self):
        return str(self.__dict__)

class SharkSchema(ma.Schema):
    class Meta:
        fields = ('name', 'age', 'year_in_zoo', 'sex', 'volume_of_aquarium', 'species', 'species_of_sharks', 'speed', 'swim_type')

shark_schema = SharkSchema()
sharks_schema = SharkSchema(many=True)
db.create_all()

@app.route("/shark", methods=["POST"])
def add_shark():
    name = request.json["name"]
    age = request.json["age"]
    year_in_zoo = request.json["year_in_zoo"]
    sex = request.json["sex"]
    volume_of_aquarium = request.json['volume_of_aquarium']
    species = request.json['species']
    species_of_sharks = request.json['species_of_sharks']
    speed = request.json['speed']
    swim_type = request.json['swim_type']
    new_shark = SharkModel(name, age, year_in_zoo, sex, volume_of_aquarium, species, species_of_sharks, speed, swim_type)

    db.session.add(new_shark)
    db.session.commit()
    return jsonify(request.json)

@app.route("/shark", methods=["GET"])
def get_sharks():
    all_sharks = SharkModel.query.all()
    return_info = sharks_schema.dump(all_sharks)
    return jsonify(return_info.data)

@app.route("/shark/<id>", methods=["GET"])
def get_shark_by_id(id):
    shark = SharkModel.query.get(id)
    return shark_schema.jsonify(shark)

@app.route("/exhibitspy/<id>", methods=["PUT"])
def update_shark(id):
    shark = SharkModel.query.get(id)
    shark.name = request.json["name"]
    shark.age = request.json["age"]
    shark.year_in_zoo = request.json["year_in_zoo"]
    shark.sex = request.json["sex"]
    shark.volume_of_aquarium = request.json["volume_of_aquarium"]
    shark.species = request.json["species"]
    shark.species_of_sharks = request.json["species_of_sharks"]
    shark.speed = request.json["speed"]
    shark.swim_type = request.json["swim_type"]

    db.session.commit()
    return shark_schema.jsonify(request.json)


@app.route("/shark/<id>", methods=["DELETE"])
def delete_shark(id):
    shark = SharkModel.query.get(id)
    db.session.delete(shark)
    db.session.commit()
    return shark_schema.jsonify(shark)

if __name__ == '__main__':
    app.run()
