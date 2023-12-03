from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

# Make a new class that inherits TokenAuthentication
# Notice that in this case, the class has the same name with TokenAuthentication with the imported TokenAuthentication from the library is renamed to BaseTokenAuth
class TokenAuthentication(BaseTokenAuth):
	# Redefine the keyword attribute
	keyword = 'Bearer'