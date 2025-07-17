from cryptography.fernet import Fernet

class TokenEncryption:
    def __init__(self, key):
        self.fernet = Fernet(key)
    def encrypt(self, token):
        return self.fernet.encrypt(token.encode()).decode()
    def decrypt(self, encrypted_token):
        return self.fernet.decrypt(encrypted_token.encode()).decode() 