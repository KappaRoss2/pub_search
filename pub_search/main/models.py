from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tab(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField('Название статьи', max_length=200)
    source = models.CharField(db_column='DOI', unique=True, max_length=200, null=True)
    preprint = models.CharField('Ссылка на препринт', max_length=200, null=True)
    copy = models.CharField('Ссылка на копию', max_length=200, null=True)
    authors = models.TextField('Список авторов', max_length=200, null=True)

    def __str__(self):
        return f'{self.title},{self.user}'


class Scimag(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    doi = models.CharField(db_column='DOI', unique=True, max_length=200)  # Field name made lowercase.
    doi2 = models.CharField(db_column='DOI2', max_length=100)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=2000)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=2000)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=10)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=10)  # Field name made lowercase.
    day = models.CharField(db_column='Day', max_length=10)  # Field name made lowercase.
    volume = models.CharField(db_column='Volume', max_length=45)  # Field name made lowercase.
    issue = models.CharField(db_column='Issue', max_length=95)  # Field name made lowercase.
    first_page = models.CharField(db_column='First_page', max_length=45)  # Field name made lowercase.
    last_page = models.CharField(db_column='Last_page', max_length=45)  # Field name made lowercase.
    journal = models.CharField(db_column='Journal', max_length=500)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=500)  # Field name made lowercase.
    issnp = models.CharField(db_column='ISSNP', max_length=11)  # Field name made lowercase.
    issne = models.CharField(db_column='ISSNE', max_length=10)  # Field name made lowercase.
    md5 = models.CharField(db_column='MD5', max_length=32)  # Field name made lowercase.
    filesize = models.PositiveIntegerField(db_column='Filesize')  # Field name made lowercase.
    timeadded = models.DateTimeField(db_column='TimeAdded')  # Field name made lowercase.
    journalid = models.CharField(db_column='JOURNALID', max_length=45)  # Field name made lowercase.
    abstracturl = models.CharField(db_column='AbstractURL', max_length=500)  # Field name made lowercase.
    attribute1 = models.CharField(db_column='Attribute1', max_length=500)  # Field name made lowercase.
    attribute2 = models.CharField(db_column='Attribute2', max_length=1000)  # Field name made lowercase.
    attribute3 = models.CharField(db_column='Attribute3', max_length=2000)  # Field name made lowercase.
    attribute4 = models.CharField(db_column='Attribute4', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    attribute5 = models.CharField(db_column='Attribute5', max_length=256)  # Field name made lowercase.
    attribute6 = models.CharField(db_column='Attribute6', max_length=45)  # Field name made lowercase.
    visible = models.CharField(max_length=3)
    pubmedid = models.CharField(db_column='PubmedID', max_length=10)  # Field name made lowercase.
    pmc = models.CharField(db_column='PMC', max_length=12)  # Field name made lowercase.
    pii = models.CharField(db_column='PII', max_length=45)  # Field name made lowercase.

    def __str__(self):
        return "%s %s" % (self.title, self.doi)

    class Meta:
        managed = False
        db_table = 'scimag'

