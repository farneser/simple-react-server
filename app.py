import sys
from server.server import start_server
from server.utils import get_ip_by_params, handle_params

if __name__ == '__main__':
    handle_params(sys.argv)
    start_server(get_ip_by_params(sys.argv))
