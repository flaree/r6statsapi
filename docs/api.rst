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
------------------

Models are classes that are received from R6Stats API.

.. automodule:: r6statsapi.Player
    :members:

.. automodule:: r6statsapi.Operators
    :members:

.. automodule:: r6statsapi.Queue
    :members:

.. automodule:: r6statsapi.Weapons
    :members:

.. automodule:: r6statsapi.Seasonal
    :members:

.. automodule:: r6statsapi.Gamemodes
    :members:

.. automodule:: r6statsapi.WeaponCategories
    :members:

.. automodule:: r6statsapi.Leaderboard
    :members:


Exceptions
----------

The following exceptions are thrown by the library.

.. automodule:: r6statsapi.errors
    :members:
    :show-inheritance:
