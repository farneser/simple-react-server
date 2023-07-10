def get_ip_by_params(argv):
    params = list(argv)

    if '-d' in params:
        return '0.0.0.0'

    return '127.0.0.1'


def handle_params(argv):
    def show_help():
        print('hi, this is simple react server')
        print('Help')
        print('-h\t - show this menu')
        print('-d\t - run server on 0.0.0.0 for docker')

    params = list(argv[1:])

    if '-h' in params:
        show_help()

    for param in params:
        if param not in ['-d', '-h']:
            show_help()
            break
