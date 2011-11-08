from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow
from pyramid.security import Everyone

class RootFactory(object):
    __acl__ = [(Allow, Everyone, 'view')]
    
    def __init__(self, request):
        pass

def groupfinder():
    pass

def includeme(config):
    authn = AuthTktAuthenticationPolicy('asd8f98ayus8fd232909309afd0923',
                                        callback=groupfinder)
    authz = ACLAuthorizationPolicy()
    
    config.set_authentication_policy(authn)
    config.set_authorization_policy(authz)
    config.set_root_factory(RootFactory)