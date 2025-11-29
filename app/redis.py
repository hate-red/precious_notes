import redis.asyncio as redis
from safir.redis import PydanticRedisStorage


r = redis.Redis()

def set_storage(datatype) -> PydanticRedisStorage:
    """
    provides storage for saving pydantic models into redis
    datatype pameter is pydantic model class 
    """
    return PydanticRedisStorage(datatype=datatype, redis=r)
     