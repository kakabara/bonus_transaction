from pymodm import errors, fields

from views import View
from models import User


class UserController:
    @staticmethod
    def auth(code: str):
        User.objects.get({''})

    @staticmethod
    def get_profile(user_id: str):
        try:
            user = User.objects.get({'_id': fields.ObjectId(user_id)})
            return View.get_response(user)
        except errors.DoesNotExist:
            return None
