from django.db import models
from django.utils.timezone import now

# Enums
class JobLocation(models.TextChoices):
    ONSITE = 'onsite', 'Onsite'
    HYBRID = 'hybrid', 'Hybrid'
    REMOTE = 'remote', 'Remote'

class JobType(models.TextChoices):
    FULLTIME = 'fulltime', 'Full-Time'
    PARTTIME = 'parttime', 'Part-Time'
    CONTRACT = 'contract', 'Contract'

# Abstract base model
class TimestampedModel(models.Model):
    id = models.AutoField(primary_key=True) 
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Models
class Job(TimestampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    job_location = models.CharField(max_length=20, choices=JobLocation.choices)
    job_type = models.CharField(max_length=20, choices=JobType.choices)
    application_link = models.URLField()

    def __str__(self):
        return self.title

class Category(TimestampedModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Partner(TimestampedModel):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.name

class Work(TimestampedModel):
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, related_name="works", blank=True)
    partners = models.ManyToManyField(Partner, related_name="work_partners", blank=True)
    image = models.ImageField(upload_to='works/')

    def __str__(self):
        return self.title

class Talent(TimestampedModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    works = models.ManyToManyField(Work, related_name="talent_works", blank=True)
    image = models.ImageField(upload_to='talents/')
    instagram = models.CharField(max_length=255, blank=True, null=True)
    x = models.CharField(max_length=255, blank=True, null=True)
    linkedIn = models.CharField(max_length=255, blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    eye_color = models.CharField(max_length=100, blank=True, null=True)
    hair = models.CharField(max_length=100, blank=True, null=True)
    dietary_requirements = models.TextField(blank=True, null=True)
    roles = models.JSONField(default=list, blank=True)
    partners = models.ManyToManyField(Partner, related_name="talent_partners", blank=True)

    def __str__(self):
        return self.name

class Blog(TimestampedModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class Booking(TimestampedModel):
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name='bookings')
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.talent.name} by {self.fullname}"
