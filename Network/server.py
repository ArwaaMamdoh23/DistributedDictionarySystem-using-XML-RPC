from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


dictionary = {}

def upload_dictionary(data):
    global dictionary
    dictionary.update(data)
    return f"Dictionary uploaded with {len(data)} words."

def get_meaning(word):
    return dictionary.get(word, "Word not found.")


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Set up server
def run_server():
    with SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler) as server:
        server.register_function(upload_dictionary, "upload_dictionary")
        server.register_function(get_meaning, "get_meaning")
        
        print("Server is running on port 9000...")
        server.serve_forever()

if __name__ == "__main__":
    run_server()

from xmlrpc.server import SimpleXMLRPCRequestHandler
import xmlrpc.client