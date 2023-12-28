from _collections_abc import dict_keys
import numpy as np
from typing import Any, overload


class superlist(list):
    def __init__(self, *args, **kwargs):
        pass

    def as_numpy(self):
        return np.array(list(self))


class superdict(dict):
    @overload
    def __init__(self, o: dict, *args, **kwargs):
        ...

    @overload
    def __init__(self, *args, **kwargs):
        ...

    def __init__(self, o: dict = None, *args, **kwargs):
        self._ignore_keys = []
        if o:
            if not isinstance(o, dict):
                raise ValueError
            for k, v in o.items():
                dict.__setitem__(self, k, v)
        dict.__setitem__(self, "_surpress_errors", kwargs.get("surpress_errors", False))
        dict.__setitem__(self, "req_type", kwargs.get("req_type"))
        self._ignore_keys.extend(["_surpress_errors", "req_type"])
        print(self._ignore_keys)
        self.update(*args, **kwargs)

    def __getattr__(self, __key):
        print(__key, "L")
        try:
            if __key in dict.get(self, "_ignore_keys"):
                raise ValueError
            return dict.__getitem__(self, __key)
        except KeyError:
            return self._raise(KeyError(__key))

    def __getitem__(self, __key: Any):
        print(__key, "K")
        try:
            if __key in dict.get(self, "_ignore_keys"):
                raise ValueError
            return dict.__getitem__(self, __key)
        except KeyError:
            return self._raise(KeyError(__key))

    def keys(self):
        dict_out = {}
        for key, value in self.__dict__.items():
            print(key)
            if key in ("req_type", "_surpress_errors"):
                continue
            else:
                dict_out[key] = value
        return dict_out.keys()

    def __setitem__(self, __key: Any, __value: Any):
        print(__key)
        return super().__setitem__(__key, __value)

    def __setattr__(self, __name, __value: Any):
        if dict.get(self, "req_type"):
            if not type(__value) == self.req_type:
                self._raise(
                    ValueError(
                        f'value of "{__name}" must be of type {self.req_type.__name__}'
                    )
                )
                return
        dict.__setitem__(self, __name, __value)

    def __repr__(self):
        repr_out = []
        ignore_keys = dict.get(self, "_ignore_keys")
        ignore_keys.append("_ignore_keys")
        for key, value in dict.items(self):
            if key in ignore_keys:
                continue
            else:
                repr_out.append(f"{repr(key)}: {repr(value)}")
        repr_out = ", ".join(repr_out)
        return f"{self.__class__.__qualname__}({{{repr_out}}})"

    def __delattr__(self, __name: str):
        return dict.__delitem__(self, __name)

    def _raise(self, err):
        if dict.get(self, "_surpress_errors"):
            return None
        else:
            raise err