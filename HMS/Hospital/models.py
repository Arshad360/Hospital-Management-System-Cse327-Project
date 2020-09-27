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


=======
departments=[('Cardiologist','Cardiologist')
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

    # corona class define
    class coronacenter(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()

    # diabetes class define
    class diabetescenter(models.Model):
        title = models.CharField(max_length=40)
        pub_date = models.DateTimeField()
        body = models.TextField()



