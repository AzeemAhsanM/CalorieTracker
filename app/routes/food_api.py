from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.database import get_db

from app.models.FoodEntry import FoodItem
from app.routes.auth import get_current_user

router = APIRouter()

@router.get("/get-calorie/{food_name}")
def get_calorie(food_name: str, db: Session = Depends(get_db)):
    food = db.query(FoodItem).filter(FoodItem.food_name.ilike(f"%{food_name}%")).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food item not found")
    return {"food": food.food_name, "calories": food.calories}

@router.get("/daily-calories")
def get_daily_calories(date_str: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # date_str should be in 'YYYY-MM-DD' format
    entries = db.query(FoodItem).filter(
        FoodItem.date == date_str,
        FoodItem.user_id == current_user.id
    ).all()
    total_calories = sum(entry.calories for entry in entries)