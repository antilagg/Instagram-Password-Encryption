## instagram `enc_password` encryption

simple tool to generate Instagram `enc_password` values using Python. mimics the browser encryption used during login.

## Setup

requirements:
- Python 3.8+
- pynacl
- cryptography

install:
pip install pynacl cryptography

## Usage

run:
```sh
python encryption.py
```
or use in your own script:

```sh
from encryption import p_encryption

enc = p_encryption(
    key_id=72,
    public_key_hex="f726cffe80513c46f1df990fe1b425758e3169b0bfd8932588b354f17e3b1b6e",
    password="your_password"
)

print(enc)
```


### Note

- use only for educational purposes 👌
