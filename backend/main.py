# main.py (dans /backend)

import sys
import os
from typing import Dict, List

# ✅ Assurer que Python voit ce dossier comme module
sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, root_validator

# ✅ Imports backend (sans prefix backend.)
from privacy_vault import PrivacyVault
from neuro_profiler import NeuroProfiler
from sensory_matrix import SensoryMatrix
from context_selector import recommander_sejour
from feddback_loop import FeedbackLoop

# ✅ Import frontend
from frontend.ui import afficher_recommandations

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# --- FastAPI ---
app = FastAPI(title="API Recommandation Séjours — NEURO ENGINE")

# --- Variables du questionnaire ---
CANONICAL_VARS = [
    "calme","nature","social","lumiere","ocean","vue","forêt","montagne","désert","campagne_vivante",
    "minimaliste","coloré","textures",
    "groupe_0_2","groupe_2_4","groupe_4_6","groupe_6_8","groupe_8_plus",
    "budget","luxe","piscine","gastronomie","retraite","spirituel","romantique","solitude",
    "nomade","eco_responsable","traditionnel","atypique","digital_detox","slow_travel",
    "animaux_bienvenus","télétravail","accessibilité","accueil_humain","communauté","enfant",
    "seul","structure","liberté","stimulation_intellectuelle","activité_physique",
    "besoin_d_isolement","besoin_de_contact","besoin_d_encadrement","accompagnement_emotionnel",
    "bruits_forts","odeurs","touchers","densité_sensorielle",
    "connexion_wifi","équipement_technologique","réalité_numérique",
    "ouvert_hiver","climat_chaud","saisonnier"
]

DEFAULT_FILL = 3.0

# --- Stockage temporaire ---
clients: List[Dict] = []
sejours: List[Dict] = []

# --- Pydantic Model ---
class Questionnaire(BaseModel):
    id: str
    variables: Dict[str, float]

    @root_validator(pre=True)
    def fill_missing(cls, values):
        vars_in = values.get("variables", {}) or {}
        for k in CANONICAL_VARS:
            vars_in[k] = float(vars_in.get(k, DEFAULT_FILL))
        values["variables"] = vars_in
        return values

# --- Init objets IA ---
vault = None
neuro = None
sensory = None
feedback_loop = None

@app.on_event("startup")
def init():
    global vault, neuro, sensory, feedback_loop
    vault = PrivacyVault()
    neuro = NeuroProfiler(vault)
    neuro.collect_data()
    sensory = SensoryMatrix()
    feedback_loop = FeedbackLoop(vault)

def to_vector(vars):
    return np.array([vars.get(k, DEFAULT_FILL) for k in CANONICAL_VARS]).reshape(1, -1)

# ✅ ROUTES API
@app.get("/")
def home():
    return {"status": "✅ API NEURO ENGINE OK"}

@app.post("/client/")
def add_client(client: Questionnaire):
    clients.append(client.dict())
    return {"added_client": client.id}

@app.post("/sejour/")
def add_sejour(sejour: Questionnaire):
    sejours.append(sejour.dict())
    return {"added_sejour": sejour.id}

@app.get("/match/{client_id}")
def match(client_id: str, top_k: int = 3, seuil: float = 0.5):
    client = next((c for c in clients if c["id"] == client_id), None)
    if not client:
        raise HTTPException(404, "Client introuvable")

    profil = neuro.get_profile_for_reco(client_id)
    c_vec = to_vector(client["variables"])

    scored = []
    for s in sejours:
        score = float(cosine_similarity(c_vec, to_vector(s["variables"]))[0,0])
        scored.append({"sejour": s, "score": score})

    recos = sorted([s for s in scored if s["score"] >= seuil], key=lambda x: x["score"], reverse=True)[:top_k]
    suggestions = [s for s in scored if s["score"] >= seuil*0.6] if len(recos) <= 1 else []

    afficher_recommandations(profil, recos, suggestions)

    return {
        "client_id": client_id,
        "profil": profil,
        "recommandations": recos,
        "suggestions": suggestions
    }
