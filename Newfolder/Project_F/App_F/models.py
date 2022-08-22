from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    contact = models.IntegerField(default=True)
    city = models.CharField(max_length=40)
    profile = models.FileField(upload_to='images/profile/')
    verification_code = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    removed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table= "User"

class Category(models.Model):
    category = models.CharField(max_length=100)
    parent_id = models.BigIntegerField()

    def __str__(self):
        return self.category

    class Meta:
        db_table = "Category"

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_description = models.TextField(max_length=300)
    comment = models.CharField(max_length=100)
    category_id = models.BigIntegerField(null=True)
    post_image = models.FileField(upload_to='media/',max_length=200, default=None)
    user_id = models.BigIntegerField(null=True)
    post_status = models.CharField(max_length=100)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    removed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title

    class Meta:
        db_table = "Post"

class Information(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    gmail = models.EmailField(unique=True)
    city = models.CharField(max_length=40)
    phone = models.IntegerField(default=True)

    def __str__(self):
        return self.fname

    class Meta:
        db_table = "Information"



