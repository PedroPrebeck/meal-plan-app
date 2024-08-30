from . import db

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    portion_size = db.Column(db.Float, nullable=False)
    protein = db.Column(db.Float, nullable=False)
    carbs = db.Column(db.Float, nullable=False)
    fats = db.Column(db.Float, nullable=False)
    calories = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    package_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"FoodItem('{self.name}', '{self.portion_size}', '{self.calories}')"