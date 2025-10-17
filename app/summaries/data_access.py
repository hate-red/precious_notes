from data_access import BaseDA
from .models import Summary


class SummaryDA(BaseDA): # type: ignore
    model = Summary
