from flask import Flask
import os

from controllers.FileController import seed_database_from_csv
from controllers.ItemController import item_controller_blueprint
from views.Item import item_views_blueprint

app = Flask(__name__)

app.register_blueprint(item_controller_blueprint)
app.register_blueprint(item_views_blueprint)

file_name = 'sample_grocery.csv'
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, file_name)
# Uncomment the following line to seed the database:
# seed_database_from_csv(file_path)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)