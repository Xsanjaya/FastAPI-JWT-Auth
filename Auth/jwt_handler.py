from base64 import decode
import time
import jwt
from utils.config import config

JWT_SECRET = config.SECRET
JWT_ALGORITHM = config.ALGORITHM

def token_response(token: str):
    return {
        "access_token" : token
    }

def signJWT(userId : str):
    payload = {
        'userId' : userId,
        'expiry' : time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
    return token
    # return token_response(token)

def decodeJWT(token : str):
    try:
      decode_token = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
      return decode_token
    #   return decode_token if decode_token['expires'] >= time.time() else None

    except:
      return {

      }

