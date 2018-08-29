from pymodm import errors

from app.view import View
from app.models import Transaction

per_page = 20


class TransactionController:
    @staticmethod
    def create(attributes_transaction: dict):
        try:
            new_transaction = Transaction(**attributes_transaction)
            new_transaction.save()
            return View.get_response(new_transaction)
        except BaseException:
            return None

    @staticmethod
    def get(card_number: str, page=1):
        try:
            cursor = Transaction.objects.raw({'card_number': card_number}).limit(per_page).skip(per_page*page)
            transactions = list(cursor)
            return View.get_response(transactions)
        except errors.DoesNotExist:
            return None
