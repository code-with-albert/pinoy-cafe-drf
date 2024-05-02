## Making Pinoy Cafe with DRF
**Install Django with pipenv**
>pipenv django

**Go to pipenv**
>pipenv shell

**Setup Project and App**
>django-admin startproject PinoyCafe .

>python manage.py startapp PinoyCafeAPI

**Select Interpreter of the created pipenv**
- ctrl + shift + p
- Select Python: Select Interpreter
- Select the pipenv virtual environment

**Create Model(Class)**

- Category
  
| **Attribute**   | **Form field type**   | **Arguments**   |
| --- | --- | --- |
| slug  | SlugField  |
| title  | CharField  | max\_length = 255; db\_index = True |

Additional:
```
def __str__(self):
    return self.title
```

- MenuItem
  
| **Attribute**   | **Form field type**   | **Arguments**   |
| --- | --- | --- |
| title  | CharField  | max\_length = 255, db\_index = True |
| price  | DecimalField  | max\_digits = 6, decimal\_places = 2 |
| featured  | BooleanField  | db\_index = True |
| category  | ForeignKey  | Category, on_delete = models.PROTECT |

Additional:
```
def __str__(self):
    return self.title
```
- NOTE: Import `User,MinValueValidator,MaxValueValidator` first as below
>from django.contrib.auth.models import User

>from django.core.validators import MinValueValidator,MaxValueValidator

- Cart
  
| **Attribute**   | **Form field type**   | **Arguments**   |
| --- | --- | --- |
| user  | ForeignKey  | User, on_delete = models.CASCADE, db_index=True |
| menuitem  | ForeignKey  | MenuItem, on_delete = models.CASCADE|
| quantity  | PositiveIntegerField  |default = 1, validators = [MinValueValidator(1), MaxValueValidator(100)]|
| unit_price  | DecimalField  | max_digits = 6, decimal_places = 2 |
| price  | DecimalField | max_digits = 6, decimal_places = 2  |

Additional:
```
def __str__(self):
    return self.user
```
To make sure the user only have 1 instance of the menuitem:
```
class Meta:
    unique_together = ('menuitem','user')
```

- Order
  
| **Attribute**   | **Form field type**   | **Arguments**   |
| --- | --- | --- |
| user  | ForeignKey  | User, on_delete = models.CASCADE, db_index = True |
| delivery_crew  | User, on_delete = models.SET_NULL,related_name='delivery_crew',null=True |
| status  | BooleanField  | default = 0, db_index=True |
| total_price  | DecimalField  | max_digits = 6, decimal_places = 2 |
| date  | DateField  | db_index = True |

Additional:
```
def __str__(self):
    return self.user + " : " + self.status + "  Date: " + self.date
```
- OrderItem

| **Attribute**   | **Form field type**   | **Arguments**   |
| --- | --- | --- |
| order  | ForeignKey  | Order, on_delete = models.CASCADE, db_index=True |
| menuitem  | ForeignKey  | MenuItem, on_delete = models.CASCADE|
| quantity  | PositiveIntegerField  |default = 1, validators = [MinValueValidator(1), MaxValueValidator(100)]|
| unit_price  | DecimalField  | max_digits = 6, decimal_places = 2 |
| price  | DecimalField | max_digits = 6, decimal_places = 2  |

Additional:
```
def __str__(self):
    return self.order
```