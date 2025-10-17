from fastapi import APIRouter

from .schemas import SentimentPublic, SentimentPost, SentimentPut
from .analyzer import SentimentAnalyzer
from .data_access import SentimentDA


router = APIRouter(prefix='/sentiment')
analyzer = SentimentAnalyzer()


@router.get('/text/{id}', response_model=SentimentPublic)
async def get_sentiment(id: int):
    """
    A function for getting sentiment analyzed text from database by it's id
    """

    instance = await SentimentDA.get(id=id)

    return instance


@router.post('/text')
async def analyze_sentiment(request_body: SentimentPost):
    """
    A function for analyzing sentiment of a given text 
    (if it was not analyzed before)
    and storing the result of that analyses to database
    """

    instance = await SentimentDA.get(**request_body.model_dump())

    # if such text was analyzed before then using its analysis result
    if instance:
        sentiments = instance.sentiments
    else:
        sentiments = analyzer.estimate_sentiment(request_body.source_text)
        sentiments_string = ' '.join(map(str, sentiments))
        # adding another filed to dict to create new database entry
        values = request_body.model_dump() | {'sentiments': sentiments_string}
        instance = await SentimentDA.create(**values)

    return instance


@router.put('/text/', response_model=SentimentPublic)
async def update_sentiment(request_body: SentimentPut):
    """
    Updating existing database entry
    """

    filter_by = {'id': request_body.id}
    updated_sentiments = analyzer.estimate_sentiment(request_body.source_text)
    values = {
        'source_text': request_body.source_text,
        'sentiments': updated_sentiments
    }
    instance = SentimentDA.update(filter_by, values)

    return instance
