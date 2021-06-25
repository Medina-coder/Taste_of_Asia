from rest_framework import serializers
from category.serializers import CategorySerializer
from commentary.serializers import CommentSerializer
from food.models import Food, Like, Image, Favorites, Foods


class FoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Foods
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Like
        fields = ('food', 'like', 'owner',)


class FavoritesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Favorites
        fields = ('food', 'favorites', 'owner',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    comments = CommentSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Food
        fields = ['title', 'body', 'price', 'quantity', 'owner', 'images', 'likes', 'comments', 'category',]

    def create(self, validated_data):
        request = self.context.get('request')
        images_data = request.FILES
        product = Food.objects.create(**validated_data)
        print(images_data.getlist('images'))
        for image in images_data.getlist('images'):
            Image.objects.create(product=product, image=image)
        return product

    def validate(self, attrs):
        return super().validate(attrs)


