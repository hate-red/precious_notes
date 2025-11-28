from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
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
    sentiments: Mapped[str]

    user: Mapped[User] = relationship('User') # type: ignore # noqa: F821


    def __str__(self) -> str:
        return f'User ID: {self.user_id} | Text: {self.source_text :20}...'
