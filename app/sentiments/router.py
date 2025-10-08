from fastapi import APIRouter


router = APIRouter(prefix='/sentiment')


@router.post('/analyze')
def analyze_sentiment():
    return {}