from data_access import BaseDA
from .models import Sentiment



class SentimentDA(BaseDA): # type: ignore
    model = Sentiment
