from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import (
    BookingCreateView, JobDetailView, JobListView, TalentListView, TalentDetailView,
    WorkListView, WorkDetailView,
    CategoryListView,
    PartnerListView,
    BlogListView, BlogDetailView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Talent API",
        default_version='v1',
        description="WTA API ",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sammiejay813@gmail.com"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Talent
    path('talents/', TalentListView.as_view(), name='talent-list'),
    path('talents/<int:pk>/', TalentDetailView.as_view(), name='talent-detail'),
    
    # Work
    path('works/', WorkListView.as_view(), name='work-list'),
    path('works/<int:pk>/', WorkDetailView.as_view(), name='work-detail'),
    
    # Category
    path('categories/', CategoryListView.as_view(), name='category-list'),
    
    # Partner
    path('partners/', PartnerListView.as_view(), name='partner-list'),
    
    # Blog
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),

    # Job
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),

    # Booking
    path('bookings/', BookingCreateView.as_view(), name='booking-create'),

    # Swagger docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
