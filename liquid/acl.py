from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from liquid.models import Base
from liquid.models import AclUsersModel
from liquid.models import AclResourcesModel

class Acl(object):
    def __init__(self, url='sqlite://', session=None):
        """
           The Acl class must either receive a url for the database engine, or
           a SqlAlchemy session instance.
        """
        if session:
            self.Session = session
        else:
            engine = create_engine(url)
            Base.metadata.create_all(engine)
            self.Session = sessionmaker(bind=engine)
        
    def add_user(self, name, parent=None):
        session = self.Session()
        acl_user = AclUsersModel(name=name)
        
        if parent:
            acl_user.parent = parent
            
        session.add(acl_user)
        session.commit()
    
    def add_resource(self, name, parent=None):
        pass
    
    def allow(self, user, resource, permissions='all'):
        pass
    
    def deny(self, user, resource, permissions='all'):
        pass