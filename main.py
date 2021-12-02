from flask import Flask, request, jsonify

from model import crud, User


app = Flask(__name__, static_folder='view', static_url_path='')


@app.route('/users/', methods=['GET'])
def get_users():
    return jsonify(crud.get_users())


@app.route('/users/<alias>', methods=['GET'])
def get_user(alias: str):
    return dict(crud.get_user(alias))


@app.route('/users/', methods=['POST'])
def create_user():
    return dict(crud.add_user(User(**request.json)))


@app.route('/users/', methods=['PUT'])
def update_user():
    return dict(crud.update_user(User(**request.json)))


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()
