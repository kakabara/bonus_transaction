from pymodm import fields, MongoModel


class Transaction(MongoModel):
    fields_to_serialize = ('card_number', 'miles', 'flying_from', 'flying_to', 'flying_date')

    card_number = fields.CharField()
    # Начисленные бонусы
    bonus = fields.FloatField(default=0)
    # полет откуда
    flying_from = fields.CharField()
    # Полет куда
    flying_to = fields.CharField()
    # дата полёта
    flying_date = fields.DateTimeField()

