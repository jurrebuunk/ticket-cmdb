from fastapi import FastAPI

app = FastAPI(title="Ticketing + CMDB")


@app.get("/health")
def health():
    return {"status": "ok"}
