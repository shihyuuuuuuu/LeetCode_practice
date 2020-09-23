class Codec:
    def __init__(self):
        self.d = {}
        self.cnt = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.d[str(self.cnt)] = longUrl
        self.cnt += 1
        return str(self.cnt-1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
