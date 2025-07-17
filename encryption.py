import os
import time
import base64
import struct
import binascii
import urllib.parse
from datetime import datetime
from nacl.public import PublicKey, SealedBox
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def p_encryption(key_id: int, public_key_hex: str, password: str, v: int = 10) -> str:
    ts = int(time.time())
    akey = os.urandom(32)
    nonce = b'\x00' * 12

    associated_data = str(ts).encode()
    aesgcm = AESGCM(akey)
    encrypted_data = aesgcm.encrypt(nonce, password.encode(), associated_data)
    ciphertext = encrypted_data[:-16]
    tg = encrypted_data[-16:]

    public_key = PublicKey(binascii.unhexlify(public_key_hex))
    sealed_box = SealedBox(public_key)
    encrypted_key = sealed_box.encrypt(akey)
    
    pl = bytearray()
    pl.append(1)
    pl.append(key_id)
    pl.extend(struct.pack('<h', len(encrypted_key)))
    pl.extend(encrypted_key)
    pl.extend(tg)
    pl.extend(ciphertext)
    fn = base64.b64encode(pl).decode()
    return f"#PWD_INSTAGRAM_BROWSER:{v}:{ts}:{fn}"


if __name__ == "__main__":
    print(p_encryption(
        72,
        "f726cffe80513c46f1df990fe1b425758e3169b0bfd8932588b354f17e3b1b6e",
        "UR_PASSWORD"
    ))
