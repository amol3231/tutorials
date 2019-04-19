# Product Service

# Import framework
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'products': ['Ice cream', 'Chocolate', 'Fruit', 'Eggs','Bread']
        }
class Users(Resource):
    def get(self):
        return {
            'Users': ['Amol', 'Anu', 'Aroob', 'Anish','Alan','Lini']
        }

# Create routes
#api.add_resource(Product, '/')
api.add_resource(Users, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
