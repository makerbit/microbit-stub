# micro:bit Stub API

This is intended as a tool for enabling autocompletion of micro:bit micropython in IDEs.

It was compiled by hand from the Scintilla autocompletion data in [mu-editor/mu][ref].
I have saved a copy of that file in `/ref` to make updating easier.

The stub includes type annotations for [Mypy][mypy]/your IDE's completion engine,
so if you have your environment set to 3.4 (to match [micropython][micropython])
you will need to install the [typing][typing-lib] library to get this to work.


[ref]: https://github.com/mu-editor/mu/blob/456943/mu/modes/api/microbit.py
[mypy]: https://mypy.readthedocs.io/en/stable/introduction.html
[micropython]: http://docs.micropython.org/en/latest/pyboard/reference/index.html
[typing-lib]: https://pypi.python.org/pypi/typing
