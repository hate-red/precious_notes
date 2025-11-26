from data_access import BaseDA
from .models import User


class UserDA(BaseDA): # type: ignore
    model = User