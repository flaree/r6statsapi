# r6statsapi
---
# Docs 
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

To install the dev version, replace `rlapi` with `git+https://github.com/flareee/r6statsapi`
```py
import r6statsapi


loop = asyncio.get_event_loop()

client = r6statsapi.Client('TOKEN')
players = loop.run_until_complete(
    client._get_weapon_stats("fiareee", Platform.uplay)
)
```

