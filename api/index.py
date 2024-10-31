import json

def handler(request):
    if request.method == 'GET':
        if request.path == '/':
            return {
                'statusCode': 200,
                'body': 'Hello, World!'
            }
        elif request.path == '/data':
            data = {
                'Review': "This DVD will be a disappointment if you get it hoping to see some substantial portion of the acts of the various comics listed on the cover. All you get here are snippets of performance, at best. The rest is just loose-leaf reminiscence about the good old days in Boston, in the early 80's, when a lot of comics were hanging out together and getting their start. It's like a frat house reunion. There's a lot of lame nostalgia. There are quite a few guffaws recalling jokes (practical and otherwise) perpetrated - back then. But you had to have been there to appreciate all the basically good ol' boy camaraderie. If you weren't actually a part of that scene, all this joshing and jostling will fall flat. If you want to actually hear some of these comics' routines - you will have to look elsewhere.",
                'prediction': 'negative',
            }
            return {
                'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}
            }
        else:
            return {
                'statusCode': 404,
                'body': '404 Not Found'
            }
    else:
        return {
            'statusCode': 405,
            'body': 'Method Not Allowed'
        }
