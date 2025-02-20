![Coverage Badge](https://img.shields.io/badge/cov-78.31-blue)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Last Commit](https://img.shields.io/github/last-commit/ma-lacroix/joshea)

## JoShea data workflow handler
<img src="app/static/images/logo.jpeg" alt="App Screenshot" width="100">

A simple Flask-based workflow orchestrator with a minimalistic UI.

### Quick install and run locally using Docker:
```sh
git clone https://github.com/ma-lacroix/joshea.git
cd joshea
make build-and-run
```
Then head to http://localhost:5000/ from your favorite browser.

### How to use
WIP - Stay tuned.

#### About: 
A personal project with the goal of creating a home-made ETL workflow orchestrator. For self-education purposes. 
I got the idea listening to [ThePrimeTime](https://www.youtube.com/@ThePrimeTimeagen/) suggesting to build your own, 
stripped-down version of the tools you use on a regular basis to deepen your understanding of the underlying challenges 
engineers faced while building them. 

I immediately thought of [Apache Airflow](https://airflow.apache.org/), 
a highly popular workflow manager that I interact with daily.   

#### Original functional requirements:
Users should be able to
- submit a new DAG
- modify an existing DAG
- see the last X runs of a DAG
- see the status of each task from any given DAG
- to delete an existing DAG

#### Original non-Functional requirements:
- A parser must be able to translate a DAG into meta data
- Tasks must be executed in order while keeping track of their statuses 
- Tasks must have a retry mechanism should it fail

###### Last updated: 2025-02-20 14:04:14
