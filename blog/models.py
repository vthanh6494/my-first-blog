from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Tag(models.Model):
    name = models.CharField(max_length=32, unique = True)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=200)
    text = RichTextUploadingField()
    text2 = RichTextUploadingField(blank=True, null=True, config_name='special',external_plugin_resources=[(
                                          'youtube',
                                          '/static/blog/vendor/ckeditor_plugins/youtube/youtube/',
                                          'plugin.js',
                                          )],
                                      )
    tags = models.ManyToManyField('Tag', related_name='posts')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    pictures = models.ImageField(default='null',upload_to='upload/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False) #True

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


