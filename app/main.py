import json

from flask import Flask, request, jsonify, render_template
from app.controllers import read_data, create_data, update_data, delete_data

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", dags_meta_info=read_data.fetch_dashboard_data())


@app.route("/r/get_next_dag_run", methods=['GET'])
def get_next_dag_run() -> json:
    dag_name = request.args.get('name')
    return jsonify(read_data.fetch_next_run(dag_name))


@app.route('/c/submit_new', methods=['POST'])
def find_new_workflows() -> json:
    return jsonify(create_data.execute_create())


@app.route('/c/schedule_dag_run', methods=['POST'])
def start_new_dag_run() -> json:
    dag_info = request.get_json()
    return jsonify(create_data.schedule_dag_run(dag_info))


@app.route('/u/execute_dag', methods=['POST'])
def run_dag() -> json:
    dag_info = request.get_json()
    return jsonify(update_data.execute_dag(dag_info.get('dag_name'), dag_info.get('id')))


@app.route('/d/remove_all', methods=['POST'])
def reset_meta_data() -> json:
    return jsonify(delete_data.flush_meta_data())


@app.route('/d/remove_dag', methods=['POST'])
def delete_dag() -> json:
    dag_info = request.get_json()
    return jsonify(delete_data.delete_workflow(dag_info.get('name')))

