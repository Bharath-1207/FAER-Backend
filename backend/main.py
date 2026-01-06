from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!", "status": "success"}
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "This is a dynamic route"}

@app.get("/home")
def function():
    return "Hello word";

@app.get("/Bharath")
def function():
    return "Bharath";

@app.get("/hari")
def function():
    return "Hello hari";

