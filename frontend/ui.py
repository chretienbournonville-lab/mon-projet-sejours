from typing import Dict, List, Tuple

def afficher_recommandations(profil: Dict, recommandations: List[Tuple[str, float]], suggestions: List[Tuple[str, float]]) -> None:
    print(f"\n--- Recommandations pour {profil.get('nom', 'utilisateur')} ---")
    if recommandations:
        print("\nSéjours fortement recommandés :")
        for nom, score in recommandations:
            print(f" - {nom} (score: {score})")
    else:
        print("Aucune recommandation forte trouvée.")

    if suggestions:
        print("\nSuggestions personnalisées :")
        for nom, score in suggestions:
            print(f" - {nom} (score: {score})")



