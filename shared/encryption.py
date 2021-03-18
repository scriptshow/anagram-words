import hashlib


def encrypt(password):
    """
    Function to encrypt the password in SHA256.

    :param password: string that will be encrypted.
    :return: SHA256 encrypted string
    """
    m = hashlib.sha256()
    m.update(password)
    return m.hexdigest()


def verify(password, encrypted):
    """
    Function to verify that the password match with the encrypted one.

    :param password: string password
    :param encrypted: SHA256 encrypted string
    :return: True or False
    """
    return encrypt(password) == encrypted
