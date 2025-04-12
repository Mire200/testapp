from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SimulationInput(BaseModel):
    joueur: str
    ligne: float
    cote: float

@router.post("/simuler")
def simuler_pari(data: SimulationInput):
    # Ta logique de probas ici (repris de Streamlit)
    return {
        "joueur": data.joueur,
        "ligne": data.ligne,
        "cote": data.cote,
        "value": 0.15,  # par exemple
        "proba": 0.62
    }