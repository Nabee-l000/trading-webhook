from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/webhook")
async def webhook(req: Request):
    data = await req.json()
    print("Received:", data)
    return {"ok": True}
