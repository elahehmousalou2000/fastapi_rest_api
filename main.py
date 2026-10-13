from fastapi import FastAPI

app = FastAPI(title="Learning REST API")

@app.get("/")
def home():
    return {"message": "Hello AI Developer"}

@app.get("/users/{name}")
def user(name: str):
    return {"name": name}
