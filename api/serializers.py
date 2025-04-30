from rest_framework import serializers
from .models import Booking, Job, Talent, Work, Category, Partner, Blog
from .mixins import ImageFieldMixin

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class PartnerSerializer(ImageFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name', 'image']

class WorkSummarySerializer(ImageFieldMixin, serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Work
        fields = ['id', 'title', 'image', 'category']

class WorkDetailSerializer(ImageFieldMixin, serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    partners = PartnerSerializer(many=True)

    class Meta:
        model = Work
        fields = ['id', 'title', 'category', 'partners', 'image',  'created_at', 'updated_at']

class TalentSummarySerializer(ImageFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = [
            'id', 'name', 'image', 'description', 'created_at', 'roles',
        ]

class TalentDetailSerializer(ImageFieldMixin, serializers.ModelSerializer):
    works = WorkSummarySerializer(many=True)
    partners = PartnerSerializer(many=True)

    class Meta:
        model = Talent
        fields = [
            'id', 'name', 'description', 'works', 'image',
            'instagram', 'x', 'linkedIn', 'facebook',
            'height', 'eye_color', 'hair', 'dietary_requirements',
            'roles', 'partners', 'created_at', 'updated_at'
        ]

class BlogSummarySerializer(ImageFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'description', 'created_at']

class BlogDetailSerializer(ImageFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'description', 'content', 'image', 'created_at', 'updated_at']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'job_type', 'job_location', 'application_link', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'talent', 'fullname', 'email', 'phone', 'event_name', 'event_date', 'additional_notes', 'created_at', 'updated_at']

    def validate_event_date(self, value):
        from django.utils.timezone import now
        if value < now().date():
            raise serializers.ValidationError("Event date cannot be in the past.")
        return value

    def validate(self, data):
        if Booking.objects.filter(talent=data['talent'], event_date=data['event_date']).exists():
            raise serializers.ValidationError({
                "event_date": f"{data['talent'].name} is already booked for this date."
            })
        return data





# from django.utils.timezone import now
# from rest_framework import serializers
# from .models import Booking, Job, Talent, Work, Category, Partner, Blog
# from .mixins import ImageFieldMixin

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'title', 'created_at', 'updated_at']

# class PartnerSerializer(ImageFieldMixin, serializers.ModelSerializer):
#     class Meta:
#         model = Partner
#         fields = ['id', 'name', 'image', 'created_at', 'updated_at']

# class WorkSerializer(ImageFieldMixin,serializers.ModelSerializer):
#     category = CategorySerializer(many=True)
#     partners = PartnerSerializer(many=True)

#     class Meta:
#         model = Work
#         fields = ['id', 'title', 'category', 'partners', 'image', 'created_at', 'updated_at']

# class TalentSerializer(ImageFieldMixin, serializers.ModelSerializer):
#     works = WorkSerializer(many=True)
#     partners = PartnerSerializer(many=True)

#     class Meta:
#         model = Talent
#         fields = [
#             'id', 'name', 'description', 'works', 'image',
#             'instagram', 'x', 'linkedIn', 'facebook',
#             'height', 'eye_color', 'hair', 'dietary_requirements',
#             'roles', 'partners', 'created_at', 'updated_at'
#         ]


# class BlogSerializer(ImageFieldMixin, serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ['id', 'title', 'author', 'description', 'content', 'image', 'created_at', 'updated_at']

# class JobSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Job
#         fields = ['id', 'title', 'description', 'job_type', 'job_location', 'application_link', 'created_at', 'updated_at']

# class BookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = ['id', 'talent', 'fullname', 'email', 'phone', 'event_name', 'event_date', 'additional_notes', 'created_at', 'updated_at']

#     def validate_event_date(self, value):
#         # Prevent booking for past dates
#         if value < now().date():
#             raise serializers.ValidationError("Event date cannot be in the past.")
#         return value

#     def validate(self, data):
#         # Ensure no duplicate booking for the same talent on the same date
#         if Booking.objects.filter(talent=data['talent'], event_date=data['event_date']).exists():
#             raise serializers.ValidationError({
#                 "event_date": f"{data['talent'].name} is already booked for this date."
#             })
#         return data






