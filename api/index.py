from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, World!')
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {
                'Review': "This DVD will be a disappointment if you get it hoping to see some substantial portion of the acts of the various comics listed on the cover. All you get here are snippets of performance, at best. The rest is just loose-leaf reminiscence about the good old days in Boston, in the early 80's, when a lot of comics were hanging out together and getting their start. It's like a frat house reunion. There's a lot of lame nostalgia. There are quite a few guffaws recalling jokes (practical and otherwise) perpetrated - back then. But you had to have been there to appreciate all the basically good ol' boy camaraderie. If you weren't actually a part of that scene, all this joshing and jostling will fall flat. If you want to actually hear some of these comics' routines - you will have to look elsewhere.",
                'prediction': 'negative',
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'404 Not Found')