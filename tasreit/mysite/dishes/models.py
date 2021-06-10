from django.db import models


class Book_your_table(models.Model):
    name = models.CharField(max_length=210, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False, default=0)
    check_in = models.CharField(max_length=120, blank=False, null=False)
    time = models.CharField(max_length=123, blank=False, null=False)
    guest = models.CharField(max_length=123, blank=False, null=False)

    def __str__(self):
        return self.name


class Our_menu(models.Model):
    name = models.CharField(max_length=123, blank=False, null=False)

    def __str__(self):
        return self.name


class Our_menu_product(models.Model):
    name = models.CharField(max_length=123, blank=False, null=False)
    Description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=0)
    our_menu = models.ForeignKey(Our_menu, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Our_Master_Chef(models.Model):
    name = models.CharField(max_length=123, blank=False, null=False)
    degree = models.CharField(max_length=123, blank=False, null=False)
    Description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)

    def __str__(self):
        return self.name


class Recent_blog(models.Model):
    name = models.CharField(max_length=123, blank=False, null=False)
    Description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)

    def __str__(self):
        return self.name


class Contact_Us(models.Model):
    name = models.CharField(max_length=123, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=123, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return self.email
