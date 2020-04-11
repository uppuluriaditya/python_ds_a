
class CaesarCipher:
    """ Class for doing encryption and decryption using a Caesar Cipher. """

    def __init__(self, shift):
        """ Construct a caesar cipher using give shift """
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)
    
    def encrypt(self, message):
        """ Returns string representing encrypted message """
        return self._transform(message, self._forward)
    
    def decrypt(self, secret):
        """ Returns the decrypted message for the encrypted secret """
        return self._transform(secret, self._backward)
    
    def _transform(self, original, code):
        """ Utility to perfrom transformation based on the given code """
        msg = list(original)
        
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)

if __name__ == "__main__":
    cipher = CaesarCipher(3)
    message = "I WANT TO BECOME A GOOD PROGRAMMER"
    encrypted_msg = cipher.encrypt(message)
    print("Encrypt: {}".format(encrypted_msg))
    decrypted_msg = cipher.decrypt(encrypted_msg)
    print("Decrypt: {}".format(decrypted_msg))
