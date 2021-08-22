import os
import sys
import warnings

if sys.path[0] in ("", os.getcwd()):
    sys.path.pop(0)


if __package__ == "":

    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)

if __name__ == "__main__":

    warnings.filterwarnings(
        "ignore", category=DeprecationWarning, module=".*packaging\\.version"
    )
    from pip._internal.cli.main import main as _main

    sys.exit(_main())
