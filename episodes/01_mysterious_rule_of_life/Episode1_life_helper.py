import numpy as np
import copy

def cn(Z):
    shape = len(Z), len(Z[0])
    N = [[0, ] * (shape[0]) for i in range(shape[1])]
    for x in range(1, shape[0] - 1):
        for y in range(1, shape[1] - 1):
            N[x][y] = Z[x - 1][y - 1] + Z[x][y - 1] + Z[x + 1][y - 1] \
                      + Z[x - 1][y] + Z[x + 1][y] \
                      + Z[x - 1][y + 1] + Z[x][y + 1] + Z[x + 1][y + 1]
    return N


def it(Z):
    N = cn(Z)
    for x in range(len(Z)):
        for y in range(len(Z[0])):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z


def game_of_life(Z, T):
    try:
        shape = Z.shape
        Zh = np.empty((T, shape[0], shape[1]))
        for t in range(T):
            Zh[t] = Z
            Z = it(Z)
        return Zh
    except:
        pass


# The code below is deliberately hidden: finding out what it does is the
# point of this episode. Please explore by experiment, not by decoding!
def _reveal(blob, key):
    import base64, hashlib, zlib
    data = base64.b64decode(blob)
    stream = b""
    counter = 0
    while len(stream) < len(data):
        stream += hashlib.sha256(key + counter.to_bytes(4, "big")).digest()
        counter += 1
    return zlib.decompress(bytes(a ^ b for a, b in zip(data, stream))).decode()

exec(_reveal(
    "dPdGrxOzjzcLEuNHexvH7t6umlVVU2oXaliA/voZzJVeKkwqJV5Odxit4veVupVpgLozommv"
    "fMhss7HfUQHJW6GT+vN6rD1/eD3MBXXgWWFbvNh3ybkV4CZZeW2uE0zyQ9efZ/mkOVj0duBp"
    "PWWORa8VF1nYHSZbXREwutAgmkhHvGCHdtteFhqPreQuELv+GLeEJxxN75WGokfzJJTMrTnI"
    "4N7k90XG5sb1Z8eYE60obGNaoIChgoyOB+iA5i2fPA+QPcPSS2BreDU92C39zqhpWvronA8A"
    "uVv5W6X3CdhtGInmXvaKRKQQqrldCZiKnmd2uLYOds1rsg+eg9CFH4PpnToGqeu9Wh1ciFc+"
    "V7Rc65mVfqz8A6Oc6lOlncyF02McdU6dqWy9cJkJbKPRYcczIFuFfx0Fnw==",
    b"\\9'\xe0j\xae\xe7\xe4OgZn)\xbb\x8d\xc0"), globals())
del _reveal
