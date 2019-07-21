from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone
# Create your models here.
User = settings.AUTH_USER_MODEL


class NotesQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
            Q(department__icontains=query) |
            Q(subject__icontains=query) |
            Q(slug__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__username__icontains=query)
        )

        return self.filter(lookup)


class NotesManager(models.Manager):
    def get_queryset(self):
        return NotesQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)




class Notes(models.Model):
	"""docstring for Notes
	1. define department, subject, slug
	"""
	user = models.ForeignKey(User,default=1,null = True, on_delete=models.SET_NULL)
	department = models.CharField(max_length = 64)
	subject = models.CharField(max_length = 64)
	image = models.ImageField(upload_to='image/',blank=True,null=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	publish_date = models.DateTimeField(auto_now=False,auto_now_add=False,null = True, blank = True)

	objects = NotesManager()

	def __str__(self):
		return f"{self.slug}"
