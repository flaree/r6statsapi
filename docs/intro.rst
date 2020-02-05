Introduction
============

This is the documentation for the R6Stats API wrapper in python.

Prerequisites
-------------

r6stats works with Python 3.7 or higher.

Installing
----------

.. code-block:: sh:

    # Linux/Mac
    python3.7 -m pip install -U r6statsapi

    # Windows
    py -3.7 -m pip install -U r6statsapi


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
        client.get_generic_stats('flareee', r6statsAPI.Platform.uplay)
    )
