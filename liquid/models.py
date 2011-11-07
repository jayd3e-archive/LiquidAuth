from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

class AclUsersModel(Base):
    __tablename__ = 'acl_users'
    
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("acl_users.id"))
    name = Column(String)
    left = Column(Integer)
    right = Column(Integer)
    parent = relationship(AclUsersModel)
    resources = association_proxy('users_resources', 'comment')

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Users('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                          self.parent_id,
                                                          self.name,
                                                          self.left,
                                                          self.right)

class AclUsersResourcesModel(Base):
    __tablename__ = 'acl_resources'
    
    user_id = Column(Integer, primary_key=True)
    resource_id = Column(Integer, ForeignKey("acl_users.id"))
    view = Column(Integer(1))
    create = Column(Integer(1))
    update = Column(Integer(1))
    delete = Column(Integer(1))
    
    user = relationship(UsersModel,
                        backref="users_resources")
    resource = relationship(IssueCommentsModel,
                            backref="users_resources"
    
    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Users('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                          self.parent_id,
                                                          self.name,
                                                          self.left,
                                                          self.right)

class AclResourcesModel(Base):
    __tablename__ = 'acl_users'
    
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("acl_users.id"))
    name = Column(String)
    left = Column(Integer)
    right = Column(Integer)
    parent = relationship(AclUsersModel)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Users('%s', '%s', '%s', '%s', '%s')>" % (self.id,
                                                          self.parent_id,
                                                          self.name,
                                                          self.left,
                                                          self.right)

