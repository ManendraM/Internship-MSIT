import pyotp
import time
Key="hi"
totp = pyotp.TOTP(Key)
print(totp.now())
