from pydantic import BaseModel


class SentimentPublic(BaseModel):
    """
    Defines response model schema
    """
    
    id: int
    user_id: int | None = None
    source_text: str
    sentiments: list[float]


class SentimentPost(BaseModel):
    """
    Defines POST request schema
    """

    user_id: int | None = None
    source_text: str


class SentimentPut(BaseModel):
    """
    Defines PUT request model schema
    source text here is an updated text that we want to reanalyze
    """

    id: int
    source_text: str


class SentimentById(BaseModel):
    """
    Defines request schema for getting sentiments by text id 
    """

    id: int
