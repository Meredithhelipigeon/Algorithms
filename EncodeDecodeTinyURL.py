class Codec:
    CodeMap="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    CodeDic={}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        s=""
        for i in longUrl[-6:] :
            s+=self.CodeMap[ord(i)%62]
        self.CodeDic[s]=longUrl    
        return s    

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.CodeDic[shortUrl]

