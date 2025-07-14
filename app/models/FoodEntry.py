from sqlalchemy import Boolean, Column, Integer, String, DateTime
from app.db.database import Base

class FoodItem(Base):
    __tablename__ = "food_items"

    id = Column(Integer, primary_key=True, index=True)
    food_name = Column(String, unique=True, nullable=False)
    calories = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False) 

    def __repr__(self):
        return f"<FoodEntry(id={self.id}, food_name={self.food_name}, calories={self.calories}, date={self.date})>"