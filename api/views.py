from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Booking, Job, Talent, Work, Category, Partner, Blog
from .serializers import BookingSerializer, JobSerializer, TalentSerializer, WorkSerializer, CategorySerializer, PartnerSerializer, BlogSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import TalentFilter

# List and Detail Views for each model
class TalentListView(ListAPIView):
    queryset = Talent.objects.all().order_by('-created_at')
    serializer_class = TalentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TalentFilter
    search_fields = ['name', 'description'] 
    ordering_fields = ['name', 'height']  

class TalentDetailView(RetrieveAPIView):
    queryset = Talent.objects.all()
    serializer_class = TalentSerializer


class WorkListView(ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category__title', 'partners__name']
    search_fields = ['title']

class WorkDetailView(RetrieveAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PartnerListView(ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class BlogListView(ListAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'content']
    ordering_fields = ['title', 'author']

class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class JobListView(ListAPIView):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['job_type', 'job_location']
    search_fields = ['title', 'description']

class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class BookingCreateView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

