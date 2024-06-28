from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 

Base = sqlalchemy.orm.declarative_base()

class Person(Base):
    __tablename__ = "persons"

    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age 
    
    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"
    
# p = Person(1, "yassine", "brigadi", "m", 22)
# print(p)

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

# p1 = Person(1, "yassine", "brigadi", "m", 22)
# p2 = Person(2, "houssam", "naimi", "m", 45)
# p3 = Person(3, "ayoub", "smaili", "m", 15)

# session.add(p1)
# session.add(p2)
# session.add(p3)
# session.commit()

# results = session.query(Person).all()
# results = session.query(Person).filter(Person.age >= 18)
# results = session.query(Person).filter(Person.firstname.like("y%"))
# results = session.query(Person).filter(Person.firstname.in_(["yassine", "achraf" , "mehdi"]))
# for res in results:
#     print(res)
