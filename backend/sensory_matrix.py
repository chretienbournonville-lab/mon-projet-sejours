from typing import List, Dict

class SensoryMatrix:
    """
    Base de données des séjours
    """
    def __init__(self):
        self.sejours = [
            {
                "id": 1,
                "nom": "Retraite Nature Luxe",
                "calme": 0.9,
                "nature": 1.0,
                "social": 0.2,
                "budget": 0.5,
                "luxe": 0.9,
                "lumiere": 0.8,
                "activites": ["yoga", "randonnée", "atelier d'écriture", "repas local"]
            },
            {
                "id": 2,
                "nom": "Aventure Éco Côtière",
                "calme": 0.5,
                "nature": 0.9,
                "social": 0.7,
                "budget": 0.7,
                "luxe": 0.3,
                "lumiere": 0.95,
                "activites": ["plongée", "surf", "repas partagés", "balades guidées"]
            },
            {
                "id": 3,
                "nom": "Weekend Zen & Sensoriel",
                "calme": 1.0,
                "nature": 0.6,
                "social": 0.1,
                "budget": 0.6,
                "luxe": 0.7,
                "lumiere": 0.7,
                "activites": ["méditation", "bains chauds", "cuisine végétale"]
            }
        ]

    def get_sejours(self) -> List[Dict]:
        return self.sejours



