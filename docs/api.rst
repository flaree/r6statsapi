API Reference
=============

Client
------

.. autoclass:: r6statsapi.Client
    :members:

Enumerations
------------

The API provides some enumerations for certain types of string to avoid the API
from being stringly typed in case the strings change in the future.

All enumerations are subclasses of `enum.Enum`.

.. autoclass:: r6statsapi.Platform
    :members:

.. autoclass:: r6statsapi.Regions
    :members:


R6Stats API Models
------------------------

Models are classes that are received from R6Stats API.

.. automodule:: r6statsapi.player
    :members:

.. automodule:: r6statsapi.operator
    :members:

.. automodule:: r6statsapi.queue
    :members:

.. automodule:: r6statsapi.weapons
    :members:

.. automodule:: r6statsapi.seasonal
    :members:

.. automodule:: r6statsapi.gamemodes
    :members:

.. automodule:: r6statsapi.weaponcategories
    :members:

.. automodule:: r6statsapi.leaderboard
    :members:

Exceptions
----------

The following exceptions are thrown by the library.

.. automodule:: r6stats.errors
    :members:
    :show-inheritance:

