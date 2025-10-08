from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional

from database import Base


class Summary(Base):
    __tablename__ = 'summaries'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # Just TEXT field to store files contents, parsed html, plain text 
    source_text: Mapped[str]
    
    # Also a TEXT filed for processed source_text
    summarized_text: Mapped[str]
    
    # Can bu null if user is not logged in 
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey('users.id'), nullable=True) # type: ignore
    
    user: Mapped['User'] = relationship('User') # type: ignore # noqa: F821


    def __str__(self) -> str:
        return f'User ID: {self.user_id} | {self.source_text :20}... | {self.summarized_text :20}...'
