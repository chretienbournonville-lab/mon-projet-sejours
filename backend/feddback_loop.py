from typing import Dict
from backend.privacy_vault import PrivacyVault  # ✅ import absolu (corrigé)

class FeedbackLoop:
    """
    Système de feedback explicite
    Gère la rétroaction des utilisateurs pour affiner les profils.
    """
    def __init__(self, vault: PrivacyVault):
        self.vault = vault

    def apply_feedback(self, user_id: str, feedback: Dict[str, float]):
        """
        Applique un feedback utilisateur (ex : le séjour était trop calme, trop social, etc.)
        et met à jour son profil dans le PrivacyVault.
        """
        # Récupérer le profil existant depuis le vault
        profile, sensitive = self.vault.get_profile(user_id)

        # Appliquer le feedback en ajustant les valeurs entre 0 et 1
        for key, value in feedback.items():
            if key in profile:
                profile[key] = min(max(profile[key] + value, 0), 1)

        # Réenregistrer le profil mis à jour
        self.vault.store_user_profile(user_id, profile, sensitive)
