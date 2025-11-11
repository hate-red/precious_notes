from fastapi import APIRouter, HTTPException, status

from .schemas import SummaryPublic, SummaryPost, SummaryUpdate, SummaryDelete
from .summarize import summarize
from .data_access import SummaryDA


router = APIRouter(prefix='/summary', tags=['Summaries'])


@router.get('/text/{id}')
async def get_summary(id: int) -> SummaryPublic:
    instance = await SummaryDA.get(id=id)
    if instance:
        return instance
    
    raise HTTPException(status.HTTP_404_NOT_FOUND)


@router.post('/text')
async def make_summary(request_body: SummaryPost) -> SummaryPublic:
    instance = await SummaryDA.get(**request_body.model_dump())
    if instance:
        return instance

    summarized_text = summarize(request_body.source_text)
    values = request_body.model_dump() | {'summarized_text': summarized_text}    
    new_instance = await SummaryDA.create(**values)
    
    return new_instance


@router.put('/text')
async def update_summary(request_body: SummaryUpdate) -> SummaryUpdate:
    filter_by = {'id': request_body.id}
    is_updated = await SummaryDA.update(
        filter_by, source_text=request_body.updated_text
    )
    
    if is_updated:
        instance = await SummaryDA.get(**filter_by)
        return instance
    
    raise HTTPException(status.HTTP_304_NOT_MODIFIED)


@router.delete('/text')
async def delete_summary(request_body: SummaryDelete) -> dict:
    is_deleted = await SummaryDA.delete(**request_body.to_dict())
    if is_deleted:
        return {'message': 'ok'}
    
    raise HTTPException(status.HTTP_404_NOT_FOUND)
