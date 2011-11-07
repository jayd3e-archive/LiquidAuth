from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

class AclUsersModel(Base):
    __tablename__ = 'acl_users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(50))
    issues = relationship(IssuesModel, backref="user")
    comments = relationship(IssueCommentsModel, backref="user")
    voted_comments = association_proxy('users_comments', 'comment')

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Users('%s', '%s', '%s')>" % (self.id,
                                              self.username,
                                              self.email)

