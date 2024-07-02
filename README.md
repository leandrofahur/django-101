# DJANGO 101

## ALGORITHM

**Step #1:** Add the instaled apps in the `$project_name/settings.py`.

```python
INSTALLED_APPS = [
 ...
 'rest_framework',
 'api',
 ]
```

**Step #2:** Create you model under the `api/models.py`.

```python
class SomeModel(models.Model):
    some_attribute = models.CharField(max_length=100)
    # attributes
    # ...

    def __str__(self):
        return self.some_attribute
```

The `__str__(self):` will allow django to display objects of that type in the admin.

**Step #3:** Apply the migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

**Step #4:** Create the respective serializer `api/serializers.py`

```python
from rest_framework import serializers
from .models import Task

class SomeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeModel
        fields = '__all__'
```

**Step #5:** Create views `api/views.py`

```python
from rest_framework import viewsets
from .models import Task
from .serializers import SomeModelSerializer

class SomeModelViewSet(viewsets.ModelViewSet):
    queryset = SomeModel.objects.all()
    serializer_class = SomeModelSerializer
```

**Step #6:** Add the urls `api/urls.py`.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SomeModelViewSet

router = DefaultRouter()
router.register(r'some_model', SomeModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

**Step #7:** Add the url with the urls from `$project_name/urls.py`.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

**Step #8:** Create a super user for the admin

```python
python manage.py createsuperuser
```

**Step #9:**

```python

```
