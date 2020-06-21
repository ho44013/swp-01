from template2 import html
from cgi import parse_qs

def application(environ, start_response):
        status = '200 OK'
        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]
	summ, prod = 0, 0
	try:
                a, b = int(a), int(b)
        	summ = a + b
        	prod = a * b
	except ValueError:
		summ = -1
		prod = -1
		if '' in [a,b]:
			summ = ' '
			prod = ' '
        response_body = html %{'sum' = summ, 'prod' = prod}

        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])
        return [response_body]

