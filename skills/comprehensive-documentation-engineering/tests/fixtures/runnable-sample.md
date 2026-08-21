# Quickstart (fixture)

A self-contained example whose code block runs standalone — used to show
`verify_examples.py --run python` reporting a clean `verified` pass.

```python
def greet(name):
    return f"Hello, {name}!"

assert greet("Ada") == "Hello, Ada!"
print(greet("Ada"))
```

The reference snippet in `clean-reference.md`, by contrast, is *illustrative*
(it references an undefined `cache` object). Running that one reports `failed` —
which is correct: illustrative reference examples are not meant to run
standalone, and the tool captures that rather than pretending it passed.
