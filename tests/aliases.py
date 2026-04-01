

# tests/aliases.py

from typing import List, Tuple, Union, Optional, Type

SampleValueLike = List[
    Tuple[Union[int, float, str, None], Optional[Type[Exception]]]
]
