from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.db.database import engine
from app.routes import auth, calorie_routes

app = FastAPI(title="Calorie Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #Replace with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Mount static files for serving frontend assets
app.mount("/static", StaticFiles(directory="app/static"), name="static")
# Set up Jinja2 templates for rendering HTML
templates = Jinja2Templates(directory="app/templates")

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(calorie_routes.router, prefix="/api/calories", tags=["Calories"])

