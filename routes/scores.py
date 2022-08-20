from flask import Blueprint, request, jsonify

from app import db
import models.score

score_app = Blueprint("score", __name__)

@score_app.route("/api/score", methods = ["GET"])
def getAllScore():
    allScore = models.score.Score.query.all()
    result = models.score.scores_schema.dump(allScore)
    return jsonify(result)

@score_app.route("/api/score/<id>", methods = ["GET"])
def getScoreById(id):
    score = models.score.Score.query.get(id)
    return models.score.score_schema.jsonify(score)

@score_app.route("/api/score", methods = ["POST"])
def addScore():
    name = request.json["name"]
    points = request.json["points"]

    tempScore = models.score.Score(name, points)

    db.session.add(tempScore)
    db.session.commit()
    return models.score.score_schema.jsonify(tempScore)

@score_app.route("/api/score/<id>", methods = ["DELETE"])
def removeScore(id):
    tempScore = models.score.Score.query.get(id)
    db.session.delete(tempScore)
    db.session.commit()
    return "Score has been removed"