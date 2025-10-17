from pydantic import BaseModel


class SummaryPublic(BaseModel):
    """
    Defines response model schema
    """
    id: int | None
    user_id: int
    source_text: str
    summarized_text: str


class SummaryPost(BaseModel):
    """
    Defines POST request model schema
    """
    user_id: int | None = None
    source_text: str


class SummaryUpdate(BaseModel):
    """
    Defines UPDATE request model 
    """
    id: int


class SummaryDelete(BaseModel):
    """
    Defines DELETE request model 
    """
    id: int
