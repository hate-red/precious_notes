from fastapi import APIRouter

from .schemas import SummaryPublic, SummaryPost, SummaryUpdate, SummaryDelete
from .summarize import summarize


router = APIRouter(prefix='/summary')


@router.post('/make')
def make_summary(request_body: SummaryPost):
    pass