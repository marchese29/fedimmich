def main() -> None:
    import uvicorn

    uvicorn.run("fedimmich.app:app", host="0.0.0.0", port=8000)
