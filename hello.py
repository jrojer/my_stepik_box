import urllib
def app(environ, start_response):
    status = '200 OK'
    headers = [ 
        ('Content-Type', 'text/plain')
    ]
    qs = urllib.parse.parse_qs(environ['QUERY_STRING'],keep_blank_values=True)
    body = '\n'.join('='.join((k,v)) for k,vl in qs.items() for v in vl)
    start_response(status, headers)
    return [bytes(body,'utf-8')]


