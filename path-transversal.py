import urllib
import requests

files = ["../server.py", "../../../../../../etc/passwd", "../../../../.bash_history"]


def try_GET():
    url = f'http://localhost:8080/{file}'
    request = urllib.request.urlopen(url)
    code = request.status

    match code:
        case 200:
            print(f"{url} is exposed to the public.")
        case 404:
            print(f"{url} is secure.")
        case 403:
            print(f"Access forbidden. But {url} is exposed")
        case 503:
            print("Service Unavailable")
        case _:
            print(f"{code} : Unknown error code")


for file in files:
    try_GET()
