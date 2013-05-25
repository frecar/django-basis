# django-basis
[![Build Status](https://travis-ci.org/frecar/django-basis.png?branch=master)](https://travis-ci.org/frecar/django-basis)

[![Coverage Status](https://coveralls.io/repos/frecar/django-basis/badge.png)](https://coveralls.io/r/frecar/django-basis)

[![PyPi version](https://pypip.in/v/django-basis/badge.png)](https://crate.io/packages/django-basis/)

[![PyPi downloads](https://pypip.in/d/django-basis/badge.png)](https://crate.io/packages/django-basis/)

## Installation
    pip install django-basis


 - Python 3 support
 - Django Customer User support

3
## Usage

```python
from basis.models import BaseModel

class Person(BaseModel):
    name = models.Cha....


person = Person()

person.save(current_user=request.user)


```
