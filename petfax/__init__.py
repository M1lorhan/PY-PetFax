from flask import Flask 
from . import pet

def create_app(): 
    app = Flask(__name__)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'
        
    # Register Blueprints
    app.register_blueprint(pet.bp)

    # Return App
    return app
