from _collections_abc import dict_keys
from typing import Any, overload

class superdict(dict):
    """A enhanced dictionary featuring attributes (variable.a = 2), specified value types

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
    >>> from pyutils import superdict
    >>> my_superdict = superdict(req_type=str)
    >>> my_superdict.a = "A"
    >>> my_superdict.two = 2 # ValueError

    consult the [docs](www.github.com/potato-pack/pyutils#readme) for more
    """

    @overload
    def __init__(self, o: dict, *args, **kwargs): ...
    @overload
    def __init__(self, *args, **kwargs): ...
    def __getattr__(self, __key): ...
    def __getitem__(self, __key: Any) -> Any: ...
    def keys(self) -> dict_keys: ...
    def __setitem__(self, __key: Any, __value: Any) -> None: ...
    def __setattr__(self, __name, __value: Any) -> None: ...
    def __repr__(self) -> str: ...
    def __delattr__(self, __name: str) -> None: ...
    def _raise(self, err): ...
