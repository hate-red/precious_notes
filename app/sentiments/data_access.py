from data_access import BaseDA
from .models import Sentiment
from .schemas import SentimentPublic


def format_instance(instance) -> SentimentPublic:
    instance.sentiments = [float(x) for x in instance.sentiments.split()]
    
    return instance


class SentimentDA(BaseDA): # type: ignore
    model = Sentiment

    @classmethod
    async def get(cls, **filter_by):
        instance = await super().get(**filter_by)
        if instance:
            instance = format_instance(instance)
        return instance
        

    @classmethod
    async def get_or_create(cls, **filter_by):
        instance = super().get_or_create(**filter_by)
        instance = format_instance(instance)
        return instance
    
    @classmethod
    async def create(cls, **filter_by):
        instance = await super().create(**filter_by)
        instance = format_instance(instance)
        return instance