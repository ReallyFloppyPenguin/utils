A enhanced dictionary featuring attributes (variable.a = 2), specified value types

#### Basic Usage:
```
>>> from pyutils import superdict
>>> my_superdict = superdict()
>>> my_superdict
superdict({})
```
# ___________________

### Main Features:
#### Attributes:
```
>>> from pyutils import superdict
>>> my_superdict = superdict()
>>> my_superdict.a = "A"
>>> my_superdict.a
A
```
# ___________________

#### Specified Value Types:
```
>>> from pyutils import superdict
>>> my_superdict = superdict(req_type=str)
>>> my_superdict.a = "A"
>>> my_superdict.two = 2 # ValueError
```
