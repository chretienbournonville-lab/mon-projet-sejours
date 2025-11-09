from typing import Dict, Tuple

class PrivacyVault:
    """
    Sépare les données sensibles et non sensibles.
    Simule un système de stockage cloisonné.
    """
    def __init__(self):
        self.profiles: Dict[str, Dict] = {}
        self.sensitive: Dict[str, Dict] = {}

    def store_user_profile(self, user_id: str, profile: Dict, sensitive_data: Dict) -> None:
        self.profiles[user_id] = profile
        self.sensitive[user_id] = sensitive_data

    def get_profile(self, user_id: str) -> Tuple[Dict, Dict]:
        return self.profiles.get(user_id, {}), self.sensitive.get(user_id, {})
