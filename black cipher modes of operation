import PIL.Image as Image
from Crypto.Cipher import AES
 
secret = Image.open('secret.png')
hfoc = Image.open('hfoc.png')
 
 
def image_encrypt(img, mode, iv, key):
    bImg = img.tobytes()
    if mode == AES.MODE_ECB:
        cipher = AES.new(key, mode)
    else:
        cipher = AES.new(key, mode, iv)
    m = cipher.encrypt(bImg)
    enc_img = Image.frombytes('RGBA', img.size, m, 'raw')
    return enc_img
 
 
print('===== ECB MODE =====')
print('HFOC:')
hfoc.show()
print('HFOC encrypted with random key:')
print('key: ' + 'tDSqLEEBjSz8MF4z')
image_encrypt(hfoc, AES.MODE_ECB, '', b'tDSqLEEBjSz8MF4z').save(
    "hfoc_ecb.png")
print('SECRET:')
secret.show()
print('SECRET encrypted with random key:')
print('key: ' + 'tDSqLEEBjSz8MF4z')
image_encrypt(secret, AES.MODE_ECB, '', b'tDSqLEEBjSz8MF4z').save(
    "secret_ecb.png")
print('===== CBC MODE =====')
print('HFOC CBC:')
image_encrypt(hfoc, AES.MODE_CBC, b'0000000000000000',
              b'0000000000000000').save("hfoc_cbc.png")
print('SECRET CBC:')
image_encrypt(secret, AES.MODE_CBC, b'0000000000000000',
              b'0000000000000000').save("secret_cbc.png")
