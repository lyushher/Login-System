from typing import List, Optional
__version__ = "21.2.4"

def main(args: Optional[List[str]] = None) -> int:

    from pip._internal.utils.entrypoints import _wrapper

    return _wrapper(args)
