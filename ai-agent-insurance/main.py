# Placeholder for AI insurance agent backend

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Insurance AI Agent API (in progress)"}
