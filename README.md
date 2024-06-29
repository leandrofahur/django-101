# DJANGO 101

## ALGORITHM

**Step #1:** Add the instaled apps in the `$project_name/settings.py`

```python
INSTALLED_APPS = [
 ...
 'rest_framework',
 'api',
 ]
```

**Step #2:** Create you model under the `api/models.py`

```python
class Some_Model(models.Model):
    some_attribute = models.CharField(max_length=100)
    # attributes
    # ...

    def __str__(self):
        return self.some_attribute
```

The `__str__(self):` will allow django to display objects of that type in the admin.

**Step #3:** Apply the migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```
