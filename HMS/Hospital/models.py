from django.db import models

""""
:Title = CharField
:Maxlength = 40
:body = Textfield

"""

    class Pharmacy(models.Model):

        title = models.CharField(max_length=40,null=True)
        pub_date = models.DateTimeField()
        body = models.TextField()

    class availablebloodGroup(models.Model):
        title = models.CharField(max_length=40,null=True)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class bloodBank(models.Model):
        title = models.CharField(max_length=40,null=True)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class coronaUpdate(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class donateBlood(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class footer(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class home(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class homeSlider(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class homeBase(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class login(models.Model):
        title = models.PositiveIntegerField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class navBar(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class notice(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()

    class Pharmacy(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()


    class saveLife(models.Model):
       title = models.CharField(max_length=40)
       pub_date = models.DateTimeField()
       body = models.TextField()


    class specialCare(models.Model):
       title = models.CharField(max_length=40, null=True)
       pub_date = models.DateTimeField()
       body = models.TextField()




