import numpy as np

class CaesarBox:
    def encode(self, msg, key):
        msg = self.split(msg, key)
        return self.encode_decode(msg, key)

    def decode(self, msg, key):
        width = self.calculate_width(msg, key)
        msg = self.split(msg, width)
        return self.encode_decode(msg, width)

    def encode_decode(self, msg, key):
        output = []

        for index, chunk in ((i, c) for i in range(0, key) for c in msg):
            try:
                output.append(chunk[index])
            except:
                pass

        return ''.join(output)

    def split(self, msg, width):
        return [msg[i:i + width] for i in range(0, len(msg), width)]

    def calculate_width(self, msg, key):
        return int(np.ceil(len(msg) / key))

key = 3

msg = "Hello World"
print ("Plain text: %s" %(msg))

c = CaesarBox()

txt = c.encode(msg, key)
print ("Encoded: %s" %(txt))

txt = c.decode(txt, key)
print ("Decoded: %s" %(txt))
