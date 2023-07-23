from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

import settings
from strategy.cls_raw import Raw
# from strategy.cls_chained import Chained

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.SQLSERVER)
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

strategy = Raw(db)

@app.route('/')
def hello():
	return {"hello": "world"}

@app.route('/pop')
def get_all():
    return strategy.all()

@app.route('/pop/<pop_id>', methods=['GET', 'DELETE'])
def crud(pop_id):
    if request.method == 'GET':
        return strategy.filter_by(pop_id)
    
    return strategy.delete_by(pop_id)

@app.route('/pop/<pop_name>/<pop_color>', methods=['PUT'])
def insert_entry(pop_name, pop_color):
    return strategy.insert_entry(pop_name, pop_color)

@app.route('/pop/<pop_id>/<pop_name>/<pop_color>', methods=['POST'])
def update_entry(pop_id, pop_name, pop_color):
    return strategy.update_entry(pop_id, pop_name, pop_color)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
