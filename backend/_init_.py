from typing import Dict, Tuple

class PrivacyVault:
    """
    Gère la séparation et anonymisation des données sensibles
    """
    def __init__(self):
        self._data_storage = {}
        self._sensitive_storage = {}

    def store_user_profile(self, user_id: str, profile_data: Dict, sensitive_data: Dict):
        self._data_storage[user_id] = profile_data
        self._sensitive_storage[user_id] = sensitive_data

    def get_profile(self, user_id: str) -> Tuple[Dict, Dict]:
        return self._data_storage.get(user_id, {}), self._sensitive_storage.get(user_id, {})

    def anonymize_profile(self, user_id: str) -> Dict:
        profile, _ = self.get_profile(user_id)
        return profile.copy()


