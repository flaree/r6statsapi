# r6statsapi
<p align="center">
<a href="https://r6statsapi.readthedocs.io/en/latest/">
    <img src="https://readthedocs.org/projects/r6statsapi/badge/">
    </a>
<a href="https://github.com/ambv/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg">
    </a>
<a href="https://pypi.org/project/r6statsapi/">
    <img src="https://badge.fury.io/py/r6statsapi.svg">
    </a>
<img src="https://github.com/flaree/r6statsapi/workflows/Black/badge.svg">
</p>

---

## Docs 
https://r6statsapi.readthedocs.io/en/latest/index.html
---
## Installation

**Python 3.7 or higher is required**

To install the library, you can just run the following command:

```sh
# Linux/Mac
python3.7 -m pip install -U r6statsapi

# Windows
py -3.7 -m pip install -U r6statsapi
```
---
## Example
```py
import r6statsapi
import asyncio


loop = asyncio.get_event_loop()

client = r6statsapi.Client('TOKEN')
players = loop.run_until_complete(
    client.get_generic_stats("flareee", r6statsapi.Platform.uplay)
)
```

