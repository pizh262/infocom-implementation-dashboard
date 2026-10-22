from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import os
import psycopg2

app = FastAPI(
    title="Infocom Implementation Dashboard API",
    description="API для панели управления внедрением ИС ООО «Инфоком-С»",
    version="1.0.0"
)

# Настройка CORS для взаимодействия с Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Infocom Implementation Dashboard API"}

@app.get("/health")
def health_check():
    """Эндпоинт для проверки работоспособности сервиса и БД"""
    db_status = "disconnected"
    database_url = os.getenv("DATABASE_URL")
    
    try:
        if database_url:
            connection = psycopg2.connect(database_url)
            cursor = connection.cursor()
            cursor.execute("SELECT 1;")
            cursor.fetchone()
            cursor.close()
            connection.close()
            db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

    return {
        "status": "healthy",
        "service": "backend",
        "database": db_status
    }
