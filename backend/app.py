from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class QuestionnaireResponse(BaseModel):
    calme: float
    nature: float
    social: float
    budget: float
    luxe: float
    lumiere: float

@app.post("/profil/neuro")
async def create_neuro_profile(response: QuestionnaireResponse):
    # Ici tu peux intégrer ta logique NeuroProfiler
    return {"message": "Profil créé avec succès", "profil": response.dict()}

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API de recommandation de séjours neuro-sensoriels."}
