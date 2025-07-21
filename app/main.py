from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import engine, SessionLocal
from sqlalchemy.orm import Session i
from typing import Annotated
from app.routes import auth, food_api 
from app.models import user, FoodEntry  # Import models to ensure they are registered with SQLAlchemy
from fastapi import APIRouter

app = FastAPI(title="Calorie Tracker API")
router = APIRouter()
#Base.metadata.create_all(bind=engine)
#app.models.Base.metadata.create_all(bind=engine)  # Create database tables based on models

# Include the authentication routes under the "/api/auth" prefix
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

app.include_router(food_api.router, prefix="/api/food", tags=["Food API"])

def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session to be used in route handlers
    finally:
        db.close()  # Ensure the session is closed after use

db_dependencies = Annotated[Session, Depends(get_db)]

