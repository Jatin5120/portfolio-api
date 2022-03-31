from flask import Flask, jsonify
import json

app = Flask(__name__)

# allData, projects = {}, []


@app.route("/")
@app.route("/home/")
@app.route("/dashboard/")
def index():
    return allData
    # return jsonify(allData)


@app.route("/project/")
@app.route("/project/<projectId>/")
def project(projectId=None):
    if projectId is None:
        return jsonify({"error": "Project id is required"})

    for project in projects:
        if project["id"] == projectId:
            return project
            # return jsonify(project)
    return jsonify({"error": "Project not found"})


@app.route("/<route>/")
def noRoute(route):
    return jsonify({"error": f"Route: '{route}' not found"})


if __name__ == "__main__":

    global allData, projects

    data = open("all.json", "r")
    allData = json.load(data)

    data = open("projects.json", "r")
    projects = json.load(data)

    app.run(debug=True)
