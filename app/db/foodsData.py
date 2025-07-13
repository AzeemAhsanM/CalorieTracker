from app.db.database import SessionLocal
from app.models.user import foodEntry

food_items = [
    {"name": "apple", "calories": 52},
    {"name": "banana", "calories": 89},
    {"name": "rice (1 cup)", "calories": 206},
    {"name": "boiled egg", "calories": 78},
    {"name": "bread slice", "calories": 66},
    {"name": "orange", "calories": 47},
    {"name": "milk (1 cup)", "calories": 103},
    {"name": "chicken breast", "calories": 165},
    {"name": "chapati", "calories": 104},
    {"name": "dal (1 cup)", "calories": 198},
    {"name": "almonds (10)", "calories": 70},
    {"name": "cheese slice", "calories": 113},
    {"name": "butter (1 tsp)", "calories": 36},
    {"name": "yogurt (1 cup)", "calories": 59},
    {"name": "potato (boiled)", "calories": 130},
    {"name": "paneer (100g)", "calories": 265},
    {"name": "mango", "calories": 99},
    {"name": "carrot", "calories": 41},
    {"name": "grapes (10)", "calories": 34},
    {"name": "peanut butter (1 tbsp)", "calories": 94}
]

db = SessionLocal()
for item in food_items:
    food = foodEntry(name=item["name"], calories=item["calories"])
    db.add(food)
db.commit()
db.close()
