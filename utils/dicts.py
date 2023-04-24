from typing import Union, Any


def get_val(collection: dict, key: Union[str, int], default='git') -> Any:
    if key in collection:
        return collection[key]
    else:
        return default
