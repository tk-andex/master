# JWT デコード

import jwt
import requests
import json
from jwt.algorithms import RSAAlgorithm

# Cognito の公開鍵を取得
keys_url = "https://cognito-idp.ap-northeast-1.amazonaws.com/ap-northeast-1_iCO7en9Y0/.well-known/jwks.json"
jwks = requests.get(keys_url).json()

# トークンをデコードする
token = "eyJraWQiOiI1dFJSWEZkRGJENEVSRjYrVzZDdkM5NHN4ZnRKSGpnb3hpMkk5ZGlZZGJBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIyN2E0N2EzOC0xMGIxLTcwZTItYTI1Zi0zYWFhNmJhNDA4MzMiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfaUNPN2VuOVkwIiwiY2xpZW50X2lkIjoiNW02Njlyb2YwbjBta3BoMTVuM2ZoM3Y0cGUiLCJvcmlnaW5fanRpIjoiZWE5MDllOTQtMjk5Yy00NGFmLTg5MjEtZTUxNDVmOWEwNzNjIiwiZXZlbnRfaWQiOiJhMzM1ODRjZC00NWE4LTRiZTEtYmNlZC1lYzc3YjYxZWU1NmMiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIiwiYXV0aF90aW1lIjoxNzQzMTM2MTIzLCJleHAiOjE3NDMxMzk3MjMsImlhdCI6MTc0MzEzNjEyMywianRpIjoiY2I3NzhlYjEtYTMwZS00ZThjLTg3YmYtN2E1ZDk3NTFhY2M4IiwidXNlcm5hbWUiOiJ0ZXN0LXVzZXIyIn0.rOCgPPi_TP4d6dwsEisuusyTnTEw8jdiJmQH5Ty8OacuaOOgFne5_eaGNToFcgEODIFFZbc59ILFM08UNH1KSOD8Ulgf51TUKksa5Mquw3rW_yqiLFnffIXeH_qGCX2bOTr1h3rzVPQa6ow-Ard62AGSX7W0PLxvFfV6W9rpsdKdHMF8Jsdzx3Q6UXQHnSkt6W6qsLMYmiTveOtKKf67VwV-g60k-MGzmY2UtU6NT-E1j8fNsSqyJYTDhvODCshZGAtgn4JxMxNDCA2KO1DWoFn_9P8DKEa6rVRidBDgcdHbe1n-v-a-mY6thF01tEcOHm4unVDciaMKp_aLlu8Gmw"

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
# {
#     'sub': '27a47a38-10b1-70e2-a25f-3aaa6ba40833',
#     'iss': 'https://cognito-idp.ap-northeast-1.amazonaws.com/ap-northeast-1_iCO7en9Y0',
#     'client_id': '5m669rof0n0mkph15n3fh3v4pe',
#     'origin_jti': 'ea909e94-299c-44af-8921-e5145f9a073c',
#     'event_id': 'a33584cd-45a8-4be1-bced-ec77b61ee56c',
#     'token_use': 'access',
#     'scope': 'aws.cognito.signin.user.admin',
#     'auth_time': 1743136123,
#     'exp': 1743139723,
#     'iat': 1743136123, 
#     'jti': 'cb778eb1-a30e-4e8c-87bf-7a5d9751acc8',
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