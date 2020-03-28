"""This is the package that contains main application."""

__title__ = 'smart_home'
__version__ = '0.0.0'
__author__ = 'marcinooo'
__maintainer__ = 'marcinooo'

from .app import (create_app,
                  db,
                  account_models,
                  home_models)

__all__ = [
    'create_app',
    'db',
    'account_models',
    'home_models'
]
