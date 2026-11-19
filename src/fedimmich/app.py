from fastapi import FastAPI

app = FastAPI(title="fedimmich")


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello, world"}
