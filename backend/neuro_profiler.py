from typing import Dict
from privacy_vault import PrivacyVault  # ✅ correction ici

class NeuroProfiler:
    """
    Collecte des données cognitives et émotionnelles.
    Simule un historique utilisateur, des réponses à un questionnaire et des observations sensibles.
    """

    def __init__(self, vault: PrivacyVault):
        self.vault = vault

    def collect_data(self) -> None:
        """
        Simule la collecte de données pour des profils utilisateurs,
        et les enregistre dans le coffre-fort de données.
        """
        profiles = [
            {
                "id": "U003",
                "nom": "flo",
                "calme": 0.7,
                "nature": 0.8,
                "social": 0.3,
                "budget": 0.6,
                "luxe": 0.8,
                "lumiere": 0.6,
            }
        ]

        sensitive_data = {
            "U002": {"fatigue": 0.3, "charge_mentale": 0.4, "saison": "été", "duree": 7},
            "U003": {"fatigue": 0.7, "charge_mentale": 0.8, "saison": "hiver", "duree": 3}
        }

        for p in profiles:
            sid = p["id"]
            self.vault.store_user_profile(sid, p, sensitive_data.get(sid, {}))
