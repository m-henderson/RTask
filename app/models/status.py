from db import Base

class Status(Base):
    __tablename__ = 'status'

    id = sa.Column(sa.BigInteger, autoincrement=True, primary_key=True)
    name = sa.Column(sa.Unicode(100), nullable=False)
