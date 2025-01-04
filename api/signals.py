from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import ImageField
from cloudinary.uploader import upload
from cloudinary.exceptions import Error as CloudinaryError

@receiver(pre_save)
def upload_image_to_cloudinary(sender, instance, **kwargs):
    """
    Automatically uploads ImageField files to Cloudinary before saving the instance.
    """
    for field in instance._meta.fields:
        if isinstance(field, ImageField):  # Check if the field is an ImageField
            image_field = getattr(instance, field.name)
            if image_field and not image_field.name.startswith("http"):  # Check if not already a URL
                try:
                    # Upload the image to Cloudinary
                    result = upload(image_field)
                    print(result)
                    # Set the Cloudinary URL back to the field
                    setattr(instance, field.name, result['secure_url'])
                except CloudinaryError as e:
                    raise ValueError(f"Cloudinary upload failed for {field.name}: {e}")
