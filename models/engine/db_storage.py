#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
import os
from models.base_model import Base, BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """Default constructor"""

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if os.getenv("HBNB_ENV ") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session

        all objects depending of the class name

        if cls=None, query all types of objects

        this method must return a dictionary:

        key = <class-name>.<object-id>

        value = object"""

        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())

        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """add the object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database
        session obj if not None"""

        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """
        close the current database connection
        and remove the reference to it
        """
        self.__session.remove()

    def reload(self):
        """create all tables in the database
        create the current database session
        by using a sessionmaker"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session
