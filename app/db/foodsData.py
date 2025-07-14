from app.db.database import SessionLocal, engine, Base
from app.models.FoodEntry import FoodItem

Base.metadata.create_all(bind=engine)  # Create database tables based on models

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
    
    # Fast food and snacks
    {"name": "pizza slice", "calories": 285},
    {"name": "cheeseburger", "calories": 303},
    {"name": "french fries (medium)", "calories": 365},
    {"name": "fried chicken (leg)", "calories": 250},
    {"name": "vegetable sandwich", "calories": 200},
    {"name": "maggi noodles", "calories": 320},
    {"name": "samosa", "calories": 262},
    {"name": "pakora", "calories": 315},
    {"name": "vada pav", "calories": 290},
    {"name": "masala dosa", "calories": 387},

    # Sweets and beverages
    {"name": "ice cream (1 scoop)", "calories": 137},
    {"name": "gulab jamun", "calories": 150},
    {"name": "laddu", "calories": 180},
    {"name": "chocolate bar", "calories": 229},
    {"name": "soft drink (1 can)", "calories": 150},
    {"name": "coffee with milk", "calories": 60},
    {"name": "tea with sugar", "calories": 50},
    {"name": "lassi (1 glass)", "calories": 230},
    {"name": "buttermilk (1 glass)", "calories": 80}
]

db = SessionLocal()
for item in food_items:
    food = FoodItem(name=item["name"], calories=item["calories"])
    db.add(food)
db.commit()
db.close()
