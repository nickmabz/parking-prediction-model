# __init__.py

# Importing custom exceptions to make them accessible as package-level imports
from .custom_exceptions import (
    ValueErrorException,
    ResourceNotFoundException,
    DBConnectionError,
    PermissionNotFoundException,
    RoleNotFoundException,
    AssociationNotFoundException,
    CampaignCategoryNotFoundException,
    # ... any other custom exceptions you have defined
)

# Importing exception handlers
from .handlers import setup_exception_handlers

# Package metadata
__version__ = '1.0.0'
__author__ = 'Joe Muigai'

# Ensure all your custom exceptions are listed in __all__ to hint to other developers
# what is expected to be available when importing * from this package.
__all__ = [
    'ValueErrorException',
    'ResourceNotFoundException',
    'DBConnectionError',
    'PermissionNotFoundException',
    'RoleNotFoundException',
    'AssociationNotFoundException',
    'CampaignCategoryNotFoundException',
    'setup_exception_handlers',
    # ... any other publicly accessible names
]
