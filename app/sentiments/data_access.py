from app.data_access import BaseDA
from app.sentiments.models import Sentiment

def format_instance(instance):
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
