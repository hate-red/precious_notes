from app.data_access import BaseDA
from app.summaries.models import Summary


class SummaryDA(BaseDA): # type: ignore
    model = Summary
