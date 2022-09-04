# https://dev.to/0xbolt/web3-authentication-on-solana-using-python-115f

# from fastapi import FastAPI
# 
# app = FastAPI()
# 
# @app.get("/")
# def root() -> None:
#     return {"message": "Web3 rocks!"}
# 
# @app.get("/verify_signature")
# def verify_signature() -> None:
#     pass

from solathon.utils import verify_signature

from fastapi import Request

@app.get("/verify_signature")
def verify_signature(request: Request) -> None:
    pass

@app.get("/verify_signature")
def verify_signature(request: Request) -> None:
    public_key = request.headers.get("public_key", None)
    # This can be passed in the "Authorization" header as well
    signature = request.headers.get("signature", None)
    try:
        verify_signature(public_key, signature)
    except:
        return {"error": "Unauthorized"}

    return {"message": public_key}

verify_signature()
