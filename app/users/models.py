from sqlalchemy.orm import mapped_column, Mapped

from database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    def __str__(self) -> str:
        return self.email
