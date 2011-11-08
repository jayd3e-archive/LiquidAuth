import unittest
from liquid.acl import Acl
from liquid.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestAcl(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        url = 'postgresql+psycopg2://jayd3e:sharpshooter7&7@localhost/liquid'
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        
        cls.url = url
        cls.engine = engine
        
    def setUp(self):
        self.Session = sessionmaker(bind=self.engine)
    
    def testInitWithoutSession(self):
        acl = Acl(url=self.url)
        self.assertTrue(acl.Session)
    
    def testInitWithSession(self):
        acl = Acl(session=self.Session())
        self.assertTrue(acl.Session)
        
    def testAddUser(self):
        session = 
        acl = Acl(url=self.url)
        acl.add_user('solid')
        
        
        