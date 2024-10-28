import os

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost") 
    DB_NAME = os.getenv("DB_NAME", "Zones")   
    DB_USER = os.getenv("DB_USER", "postgres")   
    DB_PASS = os.getenv("DB_PASS", "dost")       