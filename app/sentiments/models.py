from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from pydantic import ConfigDict
from typing import Optional

from app.database import Base
from app.users.models import User


class Sentiment(Base):
    __tablename__ = 'sentiments'

    id: Mapped[int] = mapped_column(primary_key=True)
    
    # Can bu null if user is not logged in 
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey('users.id'), nullable=True, default=None) # type: ignore
    
    # TEXT field to store files contents, parsed html, plain text 
    source_text: Mapped[str]
    
    # A string of floats like '0.2 -0.1 0.5 ..'
    # It is then converted to a list of floats
    sentiments: Mapped[str]

    user: Mapped[User] = relationship('User') # type: ignore # noqa: F821

    model_config = ConfigDict(from_attributes=True)


    def to_dict(self) -> dict:
        return {
            'id': self.id, 
            'user_id': self.user_id, 
            'source_text': self.source_text,
            'sentiments': self.sentiments,    
        }

    def __repr__(self) -> str:
        return f'User ID: {self.user_id} | '\
               f'Text: {self.source_text :10}...'\
               f'Sentiments: {self.sentiments[0]}'
