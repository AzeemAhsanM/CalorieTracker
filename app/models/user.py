from sqlalchemy import Boolean, column, Integer, ForeignKey, String
from db.database import Base

class User(Base):
    __tablename__ = "users"

    id = column(Integer, primary_key=True, index=True)
    username = column(String, unique=True, index=True)
    email = column(String, unique=True, index=True)
    hashed_password = column(String)
    is_active = column(Boolean, default=True)
    is_superuser = column(Boolean, default=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"


class foodEntry(Base):
    __tablename__ = "food_entries"

    id = column(Integer, primary_key=True, index=True)  # Primary key for food entries
    user_id = column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to users table
    food_name = column(String, index=True)
    calories = column(Integer, nullable=False)
    date = column(String, nullable=False)  # Store date as a string (e.g., "YYYY-MM-DD")

    def __repr__(self):
        return f"<FoodEntry(id={self.id}, user_id={self.user_id}, food_name={self.food_name}, calories={self.calories}, date={self.date})>"    