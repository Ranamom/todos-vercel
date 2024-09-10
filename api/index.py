from http.server import BaseHTTPRequestHandler
from urllib import parse

def handler(req, res):
    s = req.url
    dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
    res.status_code = 200
    res.headers['Content-Type'] = 'text/plain'

    if "name" in dic:
        message = "Hello, " + dic["name"] + "!"
    else:
        message = "Hello, stranger!"

    res.body = message
    return res
