import hashlib
import re


def encrypt(password):
    """
    Function to encrypt the password in SHA256.

    :param password: string that will be encrypted.
    :return: SHA256 encrypted string
    """
    m = hashlib.sha256()
    m.update(password)
    return m.hexdigest()


def verify_password_match(password, encrypted):
    """
    Function to verify that the password match with the encrypted one.

    :param password: string password
    :param encrypted: SHA256 encrypted string
    :return: True or False
    """
    return encrypt(password) == encrypted


def password_strength_check(password):
    """
    Check password strength.

    :param password: string password
    :return: True or False
    """

    # calculating the length
    length_error = len(password) < 8

    # searching for digits
    digit_error = re.search(r"\d", password) is None

    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password) is None

    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password) is None

    # searching for symbols
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    # overall result
    return not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)
