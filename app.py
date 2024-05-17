from flask import Flask
from flask_cors import CORS
from src.infrastructure.routes.routes import product_routes

app = Flask(__name__)

app.register_blueprint(product_routes, prefix='/api')

CORS(app)

if __name__ == '__main__':
    app.run()