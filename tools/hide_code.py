"""
Hide part of a Python helper file behind a light-weight encoding.

Used for "mystery" episodes, where the notebook needs to run code that
students should not simply read (e.g. a modified rule of nature).
This is NOT secure encryption: the key is in the output file, so anyone
who deliberately decodes it can read the code. It only prevents the
answer from being visible at a glance (to people or to AI assistants).

Usage:
    python tools/hide_code.py private/source.py episodes/.../helper.py

In the source file, mark the section to hide with the lines

    # --- BEGIN HIDDEN ---
    ...
    # --- END HIDDEN ---

Everything outside the markers is copied unchanged. The hidden code is
executed in the module's namespace at import time, so it can use
everything defined above it, and its functions can be imported as usual.

Keep the plaintext sources in private/ (ignored by git).
"""

import base64
import hashlib
import secrets
import sys
import zlib

BEGIN = "# --- BEGIN HIDDEN ---"
END = "# --- END HIDDEN ---"

DECODER = '''\
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
{blob},
    {key!r}), globals())
del _reveal
'''


def encode(code, key):
    data = zlib.compress(code.encode(), 9)
    stream = b""
    counter = 0
    while len(stream) < len(data):
        stream += hashlib.sha256(key + counter.to_bytes(4, "big")).digest()
        counter += 1
    return base64.b64encode(bytes(a ^ b for a, b in zip(data, stream))).decode()


def main(source_path, target_path):
    lines = open(source_path).read().splitlines(keepends=True)
    stripped = [line.rstrip() for line in lines]
    try:
        i0, i1 = stripped.index(BEGIN), stripped.index(END)
    except ValueError:
        sys.exit(f"Markers '{BEGIN}' / '{END}' not found in {source_path}")

    hidden = "".join(lines[i0 + 1:i1])
    key = secrets.token_bytes(16)
    blob = encode(hidden, key)
    blob_lines = "\n".join(f'    "{blob[i:i + 72]}"' for i in range(0, len(blob), 72))

    out = "".join(lines[:i0]) + DECODER.format(blob=blob_lines, key=key) + "".join(lines[i1 + 1:])
    open(target_path, "w").write(out)
    print(f"Wrote {target_path} ({len(hidden.splitlines())} lines hidden)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
