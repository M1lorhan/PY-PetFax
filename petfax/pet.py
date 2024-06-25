from flask import (Blueprint, render_template)
import json

with open("pets.json", "r") as f:
    pets_data = json.load(f)

#pets = json.load(open("pets.json"))

bp = Blueprint('pet', __name__, url_prefix="/pets")

# Pets routes

# Pets Index
@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets_data)

@bp.route('/<int:pet_id>')
def show_pet(pet_id):
    for pet in pets_data:
        if pet['pet_id'] == pet_id:
            return render_template('pets/show.html', pet=pet)