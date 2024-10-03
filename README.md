pip install cloudinary django-cloudinary-storage
pip install cloudinary 

INSTALLED_APPS = [
    ...
    'cloudinary',
    'cloudinary_storage',
]


cloudinary.config(
    cloud_name="",
    api_key="",
    api_secret="",
)


class MyModel(models.Model):
    image = CloudinaryField('image')


python manage.py makemigrations
python manage.py migrate
