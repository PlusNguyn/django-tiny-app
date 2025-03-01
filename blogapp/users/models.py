from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile'
                              , validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    
    def __str__(self):
        return f'{self.user.username} Profile' 
    
    # def save(self, *args, **kwargs):
    #     super(ProfileModel, self).save(*args, **kwargs)
        
    #     img = Image.open(self.image.path)
        
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)