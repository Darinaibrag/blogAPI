from rest_framework import serializers
from .models import Category, Todo, Favorites, Comment


class CategorysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Todo
        fields = '__all__'


class FavoritesTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id', 'post')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['todo_title'] = instance.todo.title
        if instance.post.preview:
            preview = instance.post.preview
            representation['todo_preview'] = preview.url
        else:
            representation['todo_preview'] = None
        return representation


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'
