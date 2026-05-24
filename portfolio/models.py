from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="E.g. Full Stack Developer")
    bio = models.TextField()
    email = models.EmailField()
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    resume_link = models.URLField(blank=True, null=True, help_text="Link to your resume (e.g. Google Drive)")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Personal Info"

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField(help_text="Proficiency from 0 to 100")
    order = models.PositiveIntegerField(default=0, help_text="Order to display skills")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Apps'),
        ('mobile', 'Mobile'),
        ('design', 'Design'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(max_length=200, help_text="E.g. Python, Django, React")
    live_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
