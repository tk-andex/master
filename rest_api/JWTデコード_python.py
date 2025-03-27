# JWT デコード

import jwt
import requests
import json
from jwt.algorithms import RSAAlgorithm

# Cognito の公開鍵を取得
keys_url = "https://cognito-idp.ap-northeast-1.amazonaws.com/ap-northeast-1_iCO7en9Y0/.well-known/jwks.json"
jwks = requests.get(keys_url).json()

# トークンをデコードする
token = "eyJraWQiOiI1dFJSWEZkRGJENEVSRjYrVzZDdkM5NHN4ZnRKSGpnb3hpMkk5ZGlZZGJBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIyN2E0N2EzOC0xMGIxLTcwZTItYTI1Zi0zYWFhNmJhNDA4MzMiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfaUNPN2VuOVkwIiwidmVyc2lvbiI6MiwiY2xpZW50X2lkIjoiNW02Njlyb2YwbjBta3BoMTVuM2ZoM3Y0cGUiLCJvcmlnaW5fanRpIjoiN2M2MmIzYzAtZWViNi00YjQ0LWIxZTQtODMzOWU2NDRkNjgwIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJwaG9uZSBvcGVuaWQgZW1haWwiLCJhdXRoX3RpbWUiOjE3NDMwNjQwOTEsImV4cCI6MTc0MzA2NzY5MSwiaWF0IjoxNzQzMDY0MDkxLCJqdGkiOiJhNmI3Y2RkNi04ZWZhLTQ2ZDEtYjFjMC04YTY0OTc3YTg0OTMiLCJ1c2VybmFtZSI6InRlc3QtdXNlcjIifQ.cy8Aj4TIU8tf9fgvaVQxniO3VPgGU-2NitLOGG-kS6T-H-GPeFpr0bn9TQO22USsKVFVQbNEg4pk8Jo9_F0RXYDtvnEsj69VgvJIPYVZeKHPt5XdWlEspi3sySergsOGVaUqTiM6-Hic_DRIC7uV4sV_-6gKoVl02ULLNws_n7d1WI9J7BJgINYrKHvAEsZz5AWt7Xs8m4wvJWdkY8ybCaWSuq74hpkjjzxbVyoFd1pa9dz9N6sQCBh8amYI95E2DreReYFvb97bCRm3eILPiC5lQYFOpSdHsJ23V-5y8IlRLMIGkTcxqxKNCILOo0lxM0GuVGVLuui96pVOzQb6dg"

# ヘッダーから 'kid' を取得
headers = jwt.get_unverified_header(token)
kid = headers["kid"]

# kid に一致する公開鍵を探す
public_key = None
for key in jwks["keys"]:
    if key["kid"] == kid:
        public_key = RSAAlgorithm.from_jwk(json.dumps(key))
        break

if public_key is None:
    raise ValueError("Public key not found.")

# トークンを検証
decoded_token = jwt.decode(
    token,
    public_key,
    algorithms=["RS256"],
    # audience="5m669rof0n0mkph15n3fh3v4pe"  # CognitoのクライアントID
)

print(decoded_token)



# レスポンス
# {'sub': '27a47a38-10b1-70e2-a25f-3aaa6ba40833', 'iss': 'https://cognito-idp.ap-northeast-1.amazonaws.com/ap-northeast-1_iCO7en9Y0', 'version': 2, 'client_id': '5m669rof0n0mkph15n3fh3v4pe', 'origin_jti': '7c62b3c0-eeb6-4b44-b1e4-8339e644d680', 'token_use': 'access', 'scope': 'phone openid email', 'auth_time': 1743064091, 'exp': 1743067691, 'iat': 1743064091, 'jti': 'a6b7cdd6-8efa-46d1-b1c0-8a64977a8493', 'username': 'test-user2'}


# 実際のkey
# {
#     "keys": [
#         {
#             "alg": "RS256",
#             "e": "AQAB",
#             "kid": "8t5opG4QWQhDKeCxp/2XtcS6ogT8wo47EKHAucwZm+4=",
#             "kty": "RSA",
#             "n": "waNjB9IuiJLvTC0jLIAlSXpUSkvi-lTnM_51xgVbzdTIsA8NazUAtLYVgij_vfpPipwHP8ap-qzVjWFzqIODGL0FDQB1A8d-SrFaFGU9_JVkt0x1bxRqHT1DuP8eCMw1jxp1mYM2myYvIW_q87tl1JPX63kkLcXBBl883f-OdxHn9gJNHsSw_fimB76gZiT7hNiM38UPM4MrBxbZjQKtp3N4UFbRQKjlYb7KUfRoGHsb7VJfjDioAHYM7RIPEr8CtGxnK4OdbIcGW3M6tDsU8WNkG9y3F1Axxv7GHKm1c3PAs0BxT3exfBYls0_5D2buSe_8nBcD-1mKayXIls_o9w",
#             "use": "sig"
#         },
#         {
#             "alg": "RS256",
#             "e": "AQAB",
#             "kid": "5tRRXFdDbD4ERF6+W6CvC94sxftJHjgoxi2I9diYdbA=",
#             "kty": "RSA",
#             "n": "wIOe1VT_4bdPb-ky3Fpykdu1PLRadgiRa0AjKpQlYB5HtsKtgQAos7NuJZrH7sdzBJx_OEdMZGAupzoLvDtze0of1Z6XsOYHqd-x-H_f84ZDKFXog2SORbr7t99CP6hLl2yBgjDQlA0OMdGRhgAPmv3uA5RjUi5T_pPq5tCbrSF-TxyRyCO5FXbTTIyNQmHmovsPLElmg4DXa7HuUgwyMM2iaCkdF4c92d5NP_xk88zLAvHQb8PQ6TWky09237rBTf1klB7GfP46PYTvsTf6ux2TwErbCOBOK5YScRip5gl_NYvI5reH3MH9Y2-V_Z1QXZGIwO2xfoIcrilVFI81VQ",
#             "use": "sig"
#         }
#     ]
# }