from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Commz Email Parser API is live"}
