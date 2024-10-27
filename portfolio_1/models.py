from django.db import models

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    hero_text = models.TextField()
    about = models.TextField()
    cv = models.FileField(upload_to='cv', blank=True)
    expertise_title = models.TextField()
    recent_work_title = models.TextField()
    get_intouch_title = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
    
    # when current portfolio is active make everything else inactive
    def save(self, *args, **kwargs):
        if self.is_active:
            Portfolio.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

class SocialLink(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.URLField()

    def __str__(self):
        return self.name


class Expertise(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.name

        

class Experience(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_present = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.company

class Education(models.Model):
    institution = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_present = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.institution

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_image', null=True, blank=True)


    @property
    def get_tags(self):
        return self.tags.split(',')


    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class SelfImage(models.Model):
    image = models.ImageField(upload_to='self_image')
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name
    
    # when current self image is active make everything else inactive
    def save(self, *args, **kwargs):
        if self.is_active:
            SelfImage.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)