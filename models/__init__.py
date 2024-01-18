#!/usr/bin/python3
"""This module instantiate an object of class FileStorages"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""unique FileStorage/DBStorage instance for all models.
"""
storage.reload()
