![Coverage Badge](https://img.shields.io/badge/cov-77.25-blue)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Last Commit](https://img.shields.io/github/last-commit/ma-lacroix/joshea)

## Jo_shea data workflow handler

### Goal: 
create a home-made ETL workflow orchestrator to deepen my understanding of such tech

### Functional requirements:
User actions:
- Be able to submit a new DAG
- Be able to modify an existing DAG
- Be able to see the last X runs of a DAG
- Be able to delete an existing DAG

DAG operations capabilities:
- Run some Python code, steps will be explicit and not rely on pre-determined operators like Airflow

User Interface:
- Minimalist: will allow users to see DAGs, their last runs and a few buttons to manipulate the DB CRUD-style. 

### Non-Functional requirements:
- Code parser must be able to translate a DAG into meta data
- Must be capable of orchestrating steps and max 3 DAGs simultaneously
- Nothing about latency, data size & scale for now
- Have a retry mechanism if a step fails

##### Language(s) used: 
Python, maybe something else eventually 

##### Backend: 
Flask, maybe some AWS database and some hosting service that can run Flask applications

###### Last updated: 2025-02-19 20:22:49
