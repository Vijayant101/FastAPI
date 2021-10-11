from fastapi import FastAPI
from routes.todos_routes import todo_api_router

app = FastAPI()

app.include_router(todo_api_router)

web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}