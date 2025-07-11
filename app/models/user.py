from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"


class foodEntry(Base):
    __tablename__ = "food_entries"

    id = Column(Integer, primary_key=True, index=True)  # Primary key for food entries
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to users table
    food_name = Column(String, index=True)
    calories = Column(Integer, nullable=False)
    date = Column(String, nullable=False)  # Store date as a string (e.g., "YYYY-MM-DD")

    def __repr__(self):
        return f"<FoodEntry(id={self.id}, user_id={self.user_id}, food_name={self.food_name}, calories={self.calories}, date={self.date})>"    