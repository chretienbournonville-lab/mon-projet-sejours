import math
from typing import Dict, List, Tuple

def ajustement_contextuel(score: float, profil: Dict) -> float:
    if profil.get("fatigue", 0) > 0.6:
        score += 0.05
    if profil.get("charge_mentale", 0) > 0.6:
        score += 0.05
    if profil.get("saison") == "hiver":
        score += 0.05
    if profil.get("duree", 0) <= 3:
        score += 0.05
    return min(score, 1.0)

def similarite_cosinus(v1: Dict[str, float], v2: Dict[str, float]) -> float:
    keys = [k for k in set(v1.keys()).intersection(v2.keys())
            if isinstance(v1[k], (int, float)) and isinstance(v2[k], (int, float))]
    if not keys:
        return 0.0
    num = sum(v1[k] * v2[k] for k in keys)
    denom1 = math.sqrt(sum(v1[k] ** 2 for k in keys))
    denom2 = math.sqrt(sum(v2[k] ** 2 for k in keys))
    if denom1 == 0 or denom2 == 0:
        return 0.0
    return num / (denom1 * denom2)

def recommander_sejour(profil: Dict, sejours: List[Dict], seuil: float = 0.5) -> List[Tuple[str, float]]:
    recommandations = []
    for s in sejours:
        sim = similarite_cosinus(profil, s)
        sim = ajustement_contextuel(sim, profil)
        if sim >= seuil:
            recommandations.append((s["nom"], round(sim, 3)))
    return sorted(recommandations, key=lambda x: x[1], reverse=True)


