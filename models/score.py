from app import db, ma

class Score(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15))
    points = db.Column(db.Integer)

    def __init__(self, name, points):
        self.name = name
        self.points = points

class ScoreSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "points")

score_schema = ScoreSchema()
scores_schema = ScoreSchema(many = True)