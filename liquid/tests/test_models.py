import unittest
from liquid.models import Base
from liquid.models import AclUsersModel
from liquid.models import AclUsersResourcesModel
from liquid.models import AclResourcesModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class TestModels(unittest.TestCase):
    def setUp(self):
        url = 'sqlite://'
        
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)
        
    def testAclUsersModel(self):
        session = self.Session()
        acl_user_group = AclUsersModel(parent_id=None,
                                       name="admin",
                                       left=1,
                                       right=4)
        
        acl_user = AclUsersModel(parent_id=None,
                                 name="solid",
                                 left=2,
                                 right=3)
                                 
        acl_user.parent = acl_user_group
        session.add(acl_user_group)
        
        session.flush()
        self.assertTrue(str(acl_user).startswith('<AclUsers'),
                        msg="str(AclUsersModel) must start with '<AclUsers'")
        self.assertEqual(acl_user.parent, acl_user_group)
        
    def testResourcesModel(self):
        session = self.Session()
        acl_resource_group = AclResourcesModel(parent_id=None,
                                               name="box",
                                               left=1,
                                               right=4)
        
        acl_resource = AclResourcesModel(parent_id=acl_resource_group.id,
                                         name="toy",
                                         left=2,
                                         right=3)
        acl_resource.parent = acl_resource_group
        session.add(acl_resource_group)
        
        session.flush()
        self.assertTrue(str(acl_resource).startswith('<AclResources'),
                        msg="str(AclResourcesModel) must start with '<AclResources'")
        self.assertEqual(acl_resource.parent, acl_resource_group)
        
    def testUsersCommentsModel(self):
        session = self.Session()
        acl_user = AclUsersModel(id=5768, 
                                 parent_id=None,
                                 name="solid",
                                 left=1,
                                 right=2)
        
        acl_resource = AclResourcesModel(id=5678,
                                         parent_id=None,
                                         name="toy",
                                         left=1,
                                         right=2)
        
        acl_user_resource = AclUsersResourcesModel(user_id=5768,
                                                   resource_id=5678)
        
        session.add(acl_user)
        session.add(acl_resource)
        session.add(acl_user_resource)
        
        session.flush()
        self.assertTrue(str(acl_user_resource).startswith('<AclUsersResources'),
                        msg="str(AclUsersResourcesModel) must start with '<AclUsersResources'")
        self.assertEqual(acl_user, acl_user_resource.users)
        self.assertIn(acl_user_resource, acl_user.users_resources)
        self.assertEqual(acl_resource, acl_user_resource.resources)
        self.assertIn(acl_user_resource, acl_resource.users_resources)
        self.assertIn(acl_resource, acl_user.resources)
        self.assertIn(acl_user, acl_resource.users)