from twisted.web.client import Agent
from twisted.web.util import redirectTo, Redirect
from encryption import Encrypt


class render:

    def __init__(self, path=None, method=None):
        self._path = path
        self._method = method


    def __call__(self, view):

        def wrapper(*args, **kwargs):
            if self._method == "GET":
                new_res = DecoratedResourceGET(executor=view(), path=self._path, exec_args=args, exec_kwargs=kwargs)
            elif self._method == "POST":
                new_res = DecoratedResourcePOST(executor=view(), path=self._path, exec_args=args, exec_kwargs=kwargs)
            else:
                raise ValueError("Uknown request method")

            return new_res

        return  wrapper


def redirect(new_url, req_data={}):
    bdata = bytes(new_url, "utf-8")
    return redirectTo(bdata)


def parse_request_args(req_args):

    #check data
    if isinstance(req_args, dict):
        decrypted = {}
        #decrypt
        for key, item in req_args.items():
            valid_key = key.decrypt("utf-8")
            valid_items = []
            for value in item:
                valid.append(value.decrypt("utf-8"))

            decrypted[valid_key] = valid_items

        return decrypted

    return None

def get_session_id(jwt_token):
    if jwt_token:
        jwt_string = jwt_token[2:len(jwt_token)-1]
        decoded_data = Encrypt.decrypt(jwt_string)
        if decoded_data:
            return decoded_data
    return None

