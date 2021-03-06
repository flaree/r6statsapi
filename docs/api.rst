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

Each class has a str() method which will return a friendly version of the enum.

.. autoclass:: r6statsapi.Platform
    :members:

.. autoclass:: r6statsapi.Regions
    :members:


R6Stats API Models
------------------

Models are classes that are received from R6Stats API.

.. automodule:: r6statsapi.player
    :members:

.. automodule:: r6statsapi.operators
    :members:

.. automodule:: r6statsapi.queue
    :members:

.. automodule:: r6statsapi.weapons
    :members:

.. automodule:: r6statsapi.seasonal
    :members:

.. automodule:: r6statsapi.gamemodes
    :members:

.. automodule:: r6statsapi.weaponCategories
    :members:

.. automodule:: r6statsapi.leaderboard
    :members:


Exceptions
----------

The following exceptions are thrown by the library.

.. automodule:: r6statsapi.errors
    :members:
    :show-inheritance:
