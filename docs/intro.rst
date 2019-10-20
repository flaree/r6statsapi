Introduction
============

This is the documentation for the R6Stats API wrapper in python.

Prerequisites
-------------

r6stats works with Python 3.7 or higher.

Installing
----------

You can get the library directly from PyPI. # SOON

Usage example
-------------

You can easily create a client using the class `r6statsapi.Client`.
Here's simple example showing how you can get player stats with this library:

.. code-block:: python3

    import asyncio
    import r6statsapi


    loop = asyncio.get_event_loop()

    client = r6statsapi.Client("TOKEN")
    players = loop.run_until_complete(
        client.get_player('fiareee', r6statsAPI.Platform.uplay)
    )
