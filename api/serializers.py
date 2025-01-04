from rest_framework import serializers
from .models import Talent, Work, Category, Partner, Blog
from .mixins import ImageFieldMixin

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class PartnerSerializer(ImageFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'image']

class WorkSerializer(ImageFieldMixin,serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    partners = PartnerSerializer(many=True)

    class Meta:
        model = Work
        fields = ['id', 'title', 'category', 'partners', 'image']

class TalentSerializer(ImageFieldMixin, serializers.ModelSerializer):
    works = WorkSerializer(many=True)
    partners = PartnerSerializer(many=True)

    class Meta:
        model = Talent
        fields = [
            'id', 'name', 'description', 'works', 'image',
            'instagram', 'x', 'linkedIn', 'facebook',
            'height', 'eye_color', 'hair', 'dietary_requirements',
            'roles', 'partners'
        ]


class BlogSerializer(ImageFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'description', 'content', 'image']





