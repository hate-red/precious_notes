from fastapi import APIRouter, HTTPException, status

from .schemas import SentimentPublic, SentimentPost, SentimentPut, SentimentDelete
from .analyzer import SentimentAnalyzer
from .data_access import SentimentDA


router = APIRouter(prefix='/sentiment', tags=['Sentiments'])
analyzer = SentimentAnalyzer()


@router.get('/text/{id}')
async def get_sentiment(id: int) -> SentimentPublic:
    """
    A function for getting sentiment analyzed text from database by it's id
    """

    instance = await SentimentDA.get(id=id)
    if instance:
        return instance

    raise HTTPException(status.HTTP_404_NOT_FOUND)


@router.post('/text')
async def analyze_sentiment(request_body: SentimentPost) -> SentimentPublic:
    """
    A function for analyzing sentiment of a given text 
    (if it was not analyzed before)
    and storing the result of that analyses to database
    """

    instance = await SentimentDA.get(**request_body.model_dump())

    # processing text if it was not analyzed before
    if not instance:
        sentiments = analyzer.estimate_sentiment(request_body.source_text)
        sentiments_string = ' '.join(map(str, sentiments))
        
        # adding another filed to dict to create new database entry
        values = request_body.model_dump() | {'sentiments': sentiments_string}
        instance = await SentimentDA.create(**values)
    
    # otherwize return existing analysis result
    return instance


@router.put('/text')
async def update_sentiment(request_body: SentimentPut) -> SentimentPublic:
    """
    Processes updated text, 
    new sentiment analysis result is updated 
    """

    filter_by = {'id': request_body.id}
    updated_sentiments = analyzer.estimate_sentiment(request_body.updated_text)
    sentiments_string = ' '.join(str(sent) for sent in updated_sentiments)

    values = {
        'source_text': request_body.updated_text,
        'sentiments': sentiments_string
    }
    is_updated = await SentimentDA.update(filter_by, **values)
    
    if is_updated:
        instance = await SentimentDA.get(**filter_by) 

        return instance

    raise HTTPException(status.HTTP_304_NOT_MODIFIED)


@router.delete('/text')
async def delete_sentiment(request_body: SentimentDelete) -> dict:
    """
    Deletes sentiment analysis by a given id or a source_text
    """
    
    is_deleted = await SentimentDA.delete(**request_body.to_dict())

    if is_deleted:
        return {'message': 'ok'}

    raise HTTPException(status.HTTP_404_NOT_FOUND)
    