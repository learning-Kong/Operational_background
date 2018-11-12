from Crypto import Random
from Crypto.PublicKey import RSA
def prvidekey():
    random_generator = Random.new().read
    rsa = RSA.generate(1024, random_generator)
    rsa_private_key = rsa.exportKey()
    rsa_public_key = rsa.key().exportKey()
    return (rsa_private_key,rsa_public_key)