from fastapi import APIRouter


router = APIRouter(prefix='/summary')


@router.post('/make')
def make_summary():
    return {}