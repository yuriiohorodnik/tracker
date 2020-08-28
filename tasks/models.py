from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class WorkerManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("User must enter email")
        if not username:
            raise ValueError("User must enter username")

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Worker(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=150, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = WorkerManager()

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(default=timezone.now)
    position = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images/avatars', blank=True)

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Project(models.Model):
    creator = models.ForeignKey("Worker", on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    description = models.TextField() # TODO TinyMCE
    slug_id = models.SlugField(max_length=255)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    theme = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    task_type = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    execution_time = models.IntegerField()
    executor_id = models.ForeignKey("Worker", on_delete=models.SET_NULL,
                                    null=True, related_name="executor_id")
    creator_id = models.ForeignKey("Worker", on_delete=models.CASCADE,
                                    related_name="creator_id")
    project_id = models.ForeignKey("Project", on_delete=models.CASCADE,
                                    related_name="project_id")


class Comment(models.Model):
    task_id = models.ForeignKey("Task", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)


class TimeLog(models.Model):
    wasted_time = models.IntegerField()
    comment = models.CharField(max_length=255)
    task = models.ForeignKey("Task", on_delete=models.DO_NOTHING)