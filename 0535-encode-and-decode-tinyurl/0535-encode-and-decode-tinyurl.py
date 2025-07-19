from random import randint
class Codec:
    def __init__(self):
        self.urls = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        coded = ""
        for i in range(6):
            coded += chr(randint(97, 123))
        self.urls[coded] = longUrl
        return coded

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.urls[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))