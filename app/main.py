from flask import Flask, request, jsonify, render_template
from controllers import read_data, create_data, update_data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", dags_meta_info=read_data.fetch_meta_data()['workflows'])


@app.route('/c/submit_new', methods=['POST'])
def find_new_workflows():
    return jsonify(create_data.execute_create())


@app.route('/r/meta_data', methods=['GET'])
def view_meta_data():
    return jsonify(read_data.fetch_meta_data())


@app.route('/u/remove_all', methods=['POST'])
def reset_meta_data():
    return jsonify(update_data.flush_meta_data())


@app.route('/u/update_existing', methods=['POST'])
def update_dag():
    pass


@app.route('/d/remove_existing', methods=['POST'])
def remove():
    pass