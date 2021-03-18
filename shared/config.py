from os import getenv

# Logging configuration variables
LOG_LEVEL_ALLOWED = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
LOG_LEVEL = getenv('ANAGRAM_LOG_LEVEL', 'INFO')

# Database configuration variables
DB_USER = getenv("ANAGRAM_DB_USER")
DB_PASS = getenv("ANAGRAM_DB_PASS")
DB_HOST = getenv("ANAGRAM_DB_HOST")
DB_PORT = getenv("ANAGRAM_DB_PORT")
DB_NAME = getenv("ANAGRAM_DB_NAME")

# Secret key
SECRET_KEY = getenv("ANAGRAM_SECRET_KEY")
