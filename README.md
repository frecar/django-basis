# django-basis
[![Build Status](https://travis-ci.org/frecar/django-basis.png?branch=master)](https://travis-ci.org/frecar/django-basis)
[![Coverage Status](https://coveralls.io/repos/frecar/django-basis/badge.png)](https://coveralls.io/r/frecar/django-basis)
[![PyPi version](https://pypip.in/v/django-basis/badge.png)](https://crate.io/packages/django-basis/)

## Installation
    pip install django-basis

 - Python versions: 2.6, 2.7, 3.2, 3.3
 - Support Django Customer User


## Usage

```python
from basis.models import BasisModel

class Person(BasisModel):
    name = models.Charfield(max_length=50)

# Save a person and register who did it
person = Person()
person.save(current_user=request.user)

# Delete person (safe_delete)
person.delete()


# Restore deleted person
person = Person.all_objects.get(id=id)
person.restore()
```
