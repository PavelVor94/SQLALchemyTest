from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db' ,echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)


    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return f"<User({self.name},{self.fullname},{self.password})>"

Base.metadata.create_all(engine)

vasiaUser = User('vasia' , 'Vasiliy Pupkin' , 'Vasia2000')
session.add(vasiaUser)
ourUser = session.query(User).filter_by(name='vasia').first()
session.add_all([User("kolia", "Cool Kolian[S.A.]","kolia$$$"), User("zina", "Zina Korzina", "zk18")])
vasiaUser.password = '-=VP2001=-'
session.commit()
