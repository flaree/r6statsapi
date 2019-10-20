# r6statsapi
---
 # Docs - TBA
```py
import r6statsapi


loop = asyncio.get_event_loop()

client = r6statsapi.Client('TOKEN')
players = loop.run_until_complete(
    client._get_weapon_stats("fiareee", Platform.uplay)
)
```

