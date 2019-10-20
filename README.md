# r6statsapi
---

```py
import r6statsapi


loop = asyncio.get_event_loop()

client = Client('TOKEN')
players = loop.run_until_complete(
    client._get_weapon_stats("fiareee", Platform.uplay)
)
```

