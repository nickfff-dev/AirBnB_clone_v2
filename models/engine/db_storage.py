#!/usr/bin/python3
"""This module defines a DBStorage class"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Create the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a class. If cls=None, query all types"""
        from models.state import State
        from models.city import City
        from models.user import User

        obj_dict = {}
        classes = {'State': State, 'City': City, 'User': User}

        if cls:
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = '{}.{}'.format(cls, obj.id)
                obj_dict[key] = obj.to_dict()
        else:
            for cls in classes.values():
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    obj_dict[key] = obj.to_dict()
        return obj_dict

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload all tables in the database"""
        from models.state import State
        from models.city import City
        from models.user import User
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
