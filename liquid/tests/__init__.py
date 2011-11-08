class SetupEnvironment(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.request = testing.DummyRequest()
        
        #Includes
        self.config.include('liquid')
        
    def tearDown(self):
        testing.tearDown()