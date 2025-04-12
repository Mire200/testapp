from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser ton frontend à parler à ton backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Remplace * par l'URL Vercel en prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend FastAPI opérationnel ✅"}
