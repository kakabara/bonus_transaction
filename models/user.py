import random
import string
from pymodm import fields, MongoModel


def generate_card_number():
    card_number_len = 10
    ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(card_number_len))


class User(MongoModel):
    fields_to_serialize = ('first_name', 'last_name', 'second_name', 'email', 'card_number', '_id')
    # Имя
    first_name = fields.CharField()
    # Фамилия
    last_name = fields.CharField()
    # Отчество
    second_name = fields.CharField()
    email = fields.EmailField()
    card_number = fields.CharField(default=generate_card_number())

    @property
    def user_id(self):
        return str(self._id)




