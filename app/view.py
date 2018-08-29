from pymodm import fields


class View:
    @staticmethod
    def serialize_entity(entity):
        """
        Метод для сериализации сущностей

        :param entity:  сущность класса из models
        :return:
        """

        def convert_field(value):
            """
            Метод для сериализация специфичных полей, к примеру ObjectID

            :param value: any
            :return: any
            """
            if isinstance(value, fields.ObjectId):
                return str(value)
            return value

        fields_to_serialize = getattr(entity, 'fields_to_serialize', None)

        if not fields_to_serialize:
            serialized = {field: convert_field(getattr(entity, field, None)) for field in entity.to_son()}
            return serialized

        serialized = {field: convert_field(getattr(entity, field, None)) for field in fields_to_serialize}
        return serialized

    @staticmethod
    def get_response(entities_or_entity, meta=None):
        """
        Метод создания response

        :param entities_or_entity: [entity] | entity
        :param meta: Данные для пагинации хранить тут
        :return: {'data': [] | {}, meta: {} | None}
        """
        response = {}
        if isinstance(entities_or_entity, list):
            response['data'] = [View.serialize_entity(entity) for entity in entities_or_entity]
        else:
            response['data'] = View.serialize_entity(entities_or_entity)
        if meta:
            response['meta'] = meta

        return response

