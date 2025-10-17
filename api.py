from fastapi import FastAPI
from pydantic import BaseModel
from models.matcher import Matcher

app = FastAPI()
m = Matcher('data/raw/mentors.csv')

class Req(BaseModel):
    topic: str
    description: str
    k: int = 5

@app.post("/match")
def match(req: Req):
    df = m.match(req.topic, req.description, req.k)
    return df.to_dict(orient='records')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app",host="0.0.0.0",port=8000)
