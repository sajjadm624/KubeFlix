from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

# In-memory "database"
users_db = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.get("/")
def read_root():
    return {"message": "Welcome to User Service"}

@app.get("/users")
def get_users():
    return users_db

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users_db if u["id"] == user_id), None)
    return user or {"error": "User not found"}

@app.post("/users")
def create_user(user: User):
    users_db.append(user.dict())
    return {"message": "User created", "user": user}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
