from sqlalchemy import ForeignKey, Column, Integer, String, Date, DateTime
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
def initializeBase(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

class AclUsersModel(Base):
    __tablename__ = 'acl_users'
    
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("acl_users.id"))
    name = Column(String)
    left = Column(Integer)
    right = Column(Integer)
    parent = relationship('AclUsersModel', uselist=False)
    resources = association_proxy('users_resources', 'resources')

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclUsers('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                             self.parent_id,
                                                             self.name,
                                                             self.left,
                                                             self.right)

class AclResourcesModel(Base):
    __tablename__ = 'acl_resources'
    
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("acl_resources.id"))
    name = Column(String)
    left = Column(Integer)
    right = Column(Integer)
    parent = relationship('AclResourcesModel', uselist=False)
    users = association_proxy('users_resources', 'users')

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclResources('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                                 self.parent_id,
                                                                 self.name,
                                                                 self.left,
                                                                 self.right)

class AclUsersResourcesModel(Base):
    __tablename__ = 'acl_users_resources'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("acl_users.id"))
    resource_id = Column(Integer, ForeignKey("acl_resources.id"))
    view = Column(Integer(1))
    create = Column(Integer(1))
    update = Column(Integer(1))
    delete = Column(Integer(1))
    
    users = relationship(AclUsersModel,
                         backref="users_resources")
    resources = relationship(AclResourcesModel,
                             backref="users_resources")
    
    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<AclUsersResources('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.user_id,
                                                                            self.resource_id,
                                                                            self.view,
                                                                            self.create,
                                                                            self.update,
                                                                            self.delete)