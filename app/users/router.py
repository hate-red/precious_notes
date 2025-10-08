from fastapi import APIRouter


router = APIRouter(prefix='/users')


@router.get('/profile')
def get_user():
    return {}
