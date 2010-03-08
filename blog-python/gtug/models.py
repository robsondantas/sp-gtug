from appengine_django.models import BaseModel
from google.appengine.ext import db

# Create your models here.
class Post(BaseModel):
    path = db.StringProperty()
    title = db.StringProperty(required=True, indexed=False)
    keywords = db.StringProperty(required=True)
    description = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    published = db.DateTimeProperty()
    updated = db.DateTimeProperty(auto_now=True)
    

