from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import foodEntry

router = APIRouter()

@router.get("/get-calorie/{food_name}")
def get_calorie(food_name: str, db: Session = Depends(get_db)):
    food = db.query(foodEntry).filter(foodEntry.name.ilike(food_name)).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food item not found")
    return {"food": food.name, "calories": food.calories}
