from twisted.web.resource import Resource

class DecoratedResourceGET(Resource):

    isLeaf = True

    def __init__(self, executor, path, exec_args, exec_kwargs):
        self._exec = executor
        self._path = path
        self.args = exec_args
        self.kwargs = exec_kwargs

    def render_GET(self, request):
        data = self._exec(request)
        return data


class DecoratedResourcePOST(Resource):

    isLeaf = True

    def __init__(self, executor, path, exec_args, exec_kwargs):
        self._exec = executor
        self._path = path
        self.args = exec_args
        self.kwargs = exec_kwargs

    def render_POST(self, request):
        data = self._exec(request)
        return data


class Server(Resource):

    def addChild(self, child):
        child = child() #make Resource instance
        self.putChild(child._path, child)
