import redis.asyncio as redis
from app.sentiments.schemas import SentimentPublic
from safir.redis import PydanticRedisStorage


r = redis.Redis()
storage = PydanticRedisStorage(datatype=SentimentPublic, redis=r)
