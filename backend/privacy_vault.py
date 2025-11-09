class PrivacyVault:
    """
    Stocke séparément les données publiques et sensibles des utilisateurs.
    """

    def __init__(self):
        self.public_data = {}
        self.sensitive_data = {}

    def store_user_profile(self, user_id: str, profile: dict, sensitive: dict):
        self.public_data[user_id] = profile
        self.sensitive_data[user_id] = sensitive

    def get_profile(self, user_id: str):
        return self.public_data.get(user_id, {}), self.sensitive_data.get(user_id, {})
