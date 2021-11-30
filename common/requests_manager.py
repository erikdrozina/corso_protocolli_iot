import requests as rq
from colorama import Fore


# handle the requests and eventually its exceptions
def send_request(method, url, resdata={}):
    try:
        # each method return a status code
        if method == 'GET':
            tmp = rq.get(url)
            return tmp.status_code
        elif method == 'POST':
            tmp = rq.post(url, json=resdata)
            return tmp.status_code
        elif method == 'PUT':
            tmp = rq.put(url, json=resdata)
            return tmp.status_code
        elif method == 'PATCH':
            tmp = rq.patch(url, json=resdata)
            return tmp.status_code
        else:
            raise SystemExit(rq.exceptions.RequestException)
    except rq.exceptions.Timeout:
        print(Fore.RED+"Connection timeout, retrying..."+Fore.RESET)
        send_request(method, url, resdata)
    except rq.exceptions.TooManyRedirects:
        print(
            Fore.RED+"Bad url, check it is indeed correct or try a different one"+Fore.RESET)
    except rq.exceptions.ConnectionError:
        print(Fore.RED+"Cannot connect to server, better luck next time..."+Fore.RESET)
    except rq.exceptions.RequestException as e:
        raise SystemExit(e)
