from rest_framework import serializers

class ImageFieldMixin(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Check if the serializer has an 'image' field
        if 'image' in representation:
            image_field = getattr(instance, 'image', None)
            if image_field:
                representation['image'] = str(image_field)  # Ensure raw Cloudinary URL
            else:
                representation['image'] = None  # Handle cases where the image is null

        return representation
