import httpx
import config


# Create the gorest manager with error handling and using the helper function approch 


def make_client():   # Creating a client in a fucntion is recommened for later changes 
    
    return httpx.Client(
        base_url = config.Base_url,
        headers = config.Headers,
        timeout = config.Timeout,
        follow_redirects=True   # Not needed for this api but generally should be added to avoid conflicts later 
    )


def make_result(ok=False,status=None,data=None,reason=None):

    return {
        'ok':ok,
        'status':status,
        'data':data,
        'reason':reason
    }



def parse_status(response):   # Found online have almost all specific erros that can come 
    code = response.status_code

    # ─── 2xx Success ──────────────────────────────
    if 200 <= code < 300:
        return None

    # ─── 4xx Client errors (specific) ─────────────
    if code == 400: return "bad_request"
    if code == 401: return "unauthorized"
    if code == 402: return "payment_required"
    if code == 403: return "forbidden"
    if code == 404: return "not_found"
    if code == 405: return "method_not_allowed"
    if code == 406: return "not_acceptable"
    if code == 408: return "request_timeout"
    if code == 409: return "conflict"
    if code == 410: return "gone"
    if code == 413: return "payload_too_large"
    if code == 415: return "unsupported_media_type"
    if code == 422: return "invalid_data"
    if code == 429: return "rate_limit"

    # ─── 5xx Server errors (specific) ─────────────
    if code == 500: return "server_error"
    if code == 501: return "not_implemented"
    if code == 502: return "bad_gateway"
    if code == 503: return "service_unavailable"
    if code == 504: return "gateway_timeout"

    # ─── Family fallbacks ─────────────────────────
    if 400 <= code < 500: return "client_error"
    if 500 <= code < 600: return "server_error"
    if 300 <= code < 400: return "redirect"
    if 100 <= code < 200: return "informational"

    return "unknown_status"


def call_api(client,method,path,**kwargs):
    try:
        response = client.request(method,path,**kwargs)
    except httpx.TimeoutException:
        return make_result(reason='timeout')
    except httpx.ConnectError:
        return make_result(reason='connection error')
    except httpx.RequestError:
        return make_result(reason='request error')

    reason = parse_status(response)

    if reason:
        return make_result(status=response.status_code,reason=reason)

    if response.status_code == 204:
        return make_result(ok=True,status=response.status_code)

    try:
        data = response.json()
    except ValueError:
        return make_result(reason='not json')

    return make_result(True,response.status_code,data)





def get_user(client,id):
    return call_api(client,'GET',f'/users/{id}')



def create_user(client,name,email,gender,status):

    payload = {
        'name':name,
        'email':email,
        'gender':gender,
        'status':status
    }

    return call_api(client,'POST','/users',json=payload)


def remove_user(client,id):
    return call_api(client,'DELETE',f'/users/{id}')


# with make_client() as client:   # This pattern should be followed when wokring with httpx client 
                                
#     # r = create_user(client,'Ali','ali4665sdffd7hidh6223wdwe69946fff46@mail.com','male','active')
#     # print(r)
    

#     s = get_user(client,8663181)
#     print(s)


#     f = remove_user(client,8663181)
#     print(f)

#     s = get_user(client,8663181)
#     print(s)
    

  

    
    