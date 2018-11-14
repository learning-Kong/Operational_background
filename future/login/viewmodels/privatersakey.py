import rsa
def prvidekey():
    (rsa_public_key, rsa_private_key) =rsa.newkeys(1024)
    return (rsa_public_key, rsa_private_key)
