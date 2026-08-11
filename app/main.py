from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello GitHub Actions"}

@app.get("/health")
def health():
    return {"status":"healthy"}
