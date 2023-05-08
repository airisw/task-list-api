from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"))
    goal = db.relationship("Goal", back_populates="tasks")

    def to_dict(self):
        if self.goal_id:
            return {
                "id": self.task_id,
                "goal_id": self.goal_id,
                "title": self.title,
                "description": self.description,
                "is_complete": False
                }
        return {
            "id": self.task_id,
            "title": self.title,
            "description": self.description,
            "is_complete": False
            }
    
    def to_dict_complete(self):
        return {
                "id": self.task_id,
                "title": self.title,
                "description": self.description,
                "is_complete": True
            }