# JWT デコード

import jwt
import requests
import json
from jwt.algorithms import RSAAlgorithm

# Cognito の公開鍵を取得
keys_url = "https://cognito-idp.ap-northeast-1.amazonaws.com/ap-northeast-1_iCO7en9Y0/.well-known/jwks.json"
jwks = requests.get(keys_url).json()

# トークンをデコードする
token = "eyJraWQiOiI1dFJSWEZkRGJENEVSRjYrVzZDdkM5NHN4ZnRKSGpnb3hpMkk5ZGlZZGJBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIyN2E0N2EzOC0xMGIxLTcwZTItYTI1Zi0zYWFhNmJhNDA4MzMiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfaUNPN2VuOVkwIiwidmVyc2lvbiI6MiwiY2xpZW50X2lkIjoiNW02Njlyb2YwbjBta3BoMTVuM2ZoM3Y0cGUiLCJvcmlnaW5fanRpIjoiYTcwOGZkN2QtMWZlMS00ODllLWJhZTEtMzE1M2ViZjFiM2U0IiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJwaG9uZSBvcGVuaWQgZW1haWwiLCJhdXRoX3RpbWUiOjE3NDMwNDMwMDMsImV4cCI6MTc0MzA0NjYwMywiaWF0IjoxNzQzMDQzMDAzLCJqdGkiOiIxMjM5YWY5Ni0wOTM3LTRmYzQtYTc3ZC03Zjg5YWFmNzU0NDMiLCJ1c2VybmFtZSI6InRlc3QtdXNlcjIifQ.pM_QrzY-L3N1SHdZKiztyPdcZWuKxYd6GOGUB38udToN5zYIWKFWwW5iGNNqOrpusMDdhlc5dV0ee9G_crx5T1xWZNVAtyIvbayToIwn-WyTjjnZgPZBewluDCWLTC6sJqWUohAy1Cq2aAVBOFzy5HM0JT-82ostJIXkPOklwHa7I736unFD1BCKygXuDgDUIGFOKwGJTGoG_wvT6LBWquDsHeAHFrJDJ8ZY4f-YcAJ4MBYwaGEgyEyMgyq4M9Xog6P8ayiEXp6s-ChC6DxUQx34CyW1uRu842fEMNZHRq5GVBg6yuOWrA_1h5uVZc6ZiFLiVr78pGO2d3KcXV40DA"

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
# {'sub': 
#     '27a47a38-10b1-70e2-a25f-3aaa6ba40833',
#     'iss': 'https://cognito-idp.ap-northeast-1.amazonaws.com/ap-northeast-1_iCO7en9Y0',
#     'version': 2,
#     'client_id': '5m669rof0n0mkph15n3fh3v4pe',
#     'origin_jti': 'a708fd7d-1fe1-489e-bae1-3153ebf1b3e4',
#     'token_use': 'access',
#     'scope': 'phone openid email',
#     'auth_time': 1743043003,
#     'exp': 1743046603,
#     'iat': 1743043003,
#     'jti': '1239af96-0937-4fc4-a77d-7f89aaf75443',
#     'username': 'test-user2'
# }


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