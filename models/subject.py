from sqlalchemy import Integer, Column, Text, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

association_table = Table(
    "association",
    Base.metadata,
    Column("subject_id", Integer, ForeignKey("subject.id")),
    Column("group_id", Integer, ForeignKey("groups.id"))
)


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    groups = relationship("Gruop", secondary=association_table, backref="group_subject")

