from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db.database import engine, SessionLocal, Session
from typing import Annotated, Depends
from app.routes import auth, calorie_routes
from app.models import user, food_entry  # Import models to ensure they are registered with SQLAlchemy

app = FastAPI(title="Calorie Tracker API")
app.models.Base.metadata.create_all(bind=engine)  # Create database tables based on models

# Enable Cross-Origin Resource Sharing to allow frontend (on another domain/port) to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development); use specific domain in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Mount static files so they can be served under the "/static" path
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configure the templates folder for rendering dynamic HTML pages using Jinja2
templates = Jinja2Templates(directory="app/templates")

# Include the authentication routes under the "/api/auth" prefix
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

# Include the calorie-related routes under the "/api/calories" prefix
app.include_router(calorie_routes.router, prefix="/api/calories", tags=["Calories"])

def get_db():
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session to be used in route handlers
    finally:
        db.close()  # Ensure the session is closed after use

db_dependencies = Annotated[Session, Depends(get_db)]

