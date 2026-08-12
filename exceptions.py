from fastapi.responses import JSONResponse
from fastapi import Request

class PinCodeNotFoundError(Exception):
    def __init__(self, pincode:str):
        self.pincode=pincode
    
class InvalidPinCodeError(Exception):
    def __init__(self,pincode:str,reason:str ="Invalid format"):
        self.pincode=pincode
        self.reason=reason
        
#Custom Handler

async def pincode_not_found_handler(reqest:Request , exc : PinCodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"pincode_not_found",
            "message":f"No location for pincode : {exc.pincode}",
            "pincode":exc.pincode
        }
    )
        

async def invalid_pincode_handler(reqest:Request , exc : InvalidPinCodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error":"Invalid_pincode",
            "message":f"Pincode '{exc.pincode}' is invalid: {exc.reason}",
            "pincode":exc.pincode
        }
    )
        