import urllib
def app(environ, start_response):
    status = '200 OK'
    headers = [ 
        ('Content-Type', 'text/plain')
    ]
    qs = urllib.parse.parse_qs(environ['QUERY_STRING'])
    body = '\n'.join('='.join((k,v[0])) for k,v in qs.items())
    start_response(status, headers)
    return [bytes(body,'utf-8')]


