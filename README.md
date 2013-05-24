# django-basis

## Installation
    pip install django-basis


Support Customer user

## Usage

```python
from basis.models import BaseModel

class Person(BaseModel):
    name = models.Cha....


person = Person()

person.save(current_user=request.user)


```
