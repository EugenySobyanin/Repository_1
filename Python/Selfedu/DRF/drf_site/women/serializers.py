import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from .models import Women


"""Пример работы сериализатора с обычными классами."""


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


# Демонстация как работает сериализатор. Сериализует из модели в python словарь
# Проверить работу можно через shell
def encode():
    model = WomenModel('Key', 'Content: value')
    model_sr = WomenSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)


# Обратный пример: из Json в модель
def decode():
    stream = io.BytesIO(b'{"title": "Nataly Portman", "content": "Content"}')
    data = JSONParser().parse(stream)
    print(data, type(data), sep=" | ")
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    # validated_data - упорядоченый словарь - результат десериализации
    print(serializer.validated_data, type(serializer.validated_data), sep=" | ")






# class WomenSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Women
#         fields = ('title', 'cat_id')
