from flask import Flask, jsonify
import json

app = Flask(__name__)


def setData():
    global allData, projects

    data = open("all.json", "r")
    allData = json.load(data)

    data = open("projects.json", "r")
    projects = json.load(data)


def getError(error="Invalid request", message="Unknown error occured."):
    return jsonify({"error": error, "message": message})


@app.route("/")
@app.route("/home/")
@app.route("/dashboard/")
def index():
    global allData

    return jsonify(allData)


@app.route("/project/")
@app.route("/project/<projectId>/")
def project(projectId=None):
    global projects

    if projectId is None:
        return getError(error="Invalid request", message="Project ID is missing")

    for project in projects:
        if project["id"] == projectId:

            return jsonify(project)

    return getError(error="Wrong Project ID", message="Project not found")


@app.route("/<route>/")
@app.route("/<route>/<projectId>/")
def noRoute(route, projectId=None):
    return getError(error="Invalid route", message=f"Route '{route}' not found")


if __name__ == "__main__":
    allData, projects = {}, []
    setData()

    app.run(debug=True)
