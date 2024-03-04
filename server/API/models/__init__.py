from .db import db_init_app

from .User import UserModel, UserExceptions
from .JWTBlocklist import JWTList, JWTExceptions
# other models import


# Must also inherit other future imported exceptions
class DBExceptions(UserExceptions, JWTExceptions): 
    pass
