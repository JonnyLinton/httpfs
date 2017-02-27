"""Usage:
  httpfs --help
  httpfs [-v] [-p PORT] [-d DIR]

Options:
  --help     Show this screen.
  -v         Prints debugging messages.
  -p PORT    Specifies the port number that the server will listen
             and serve at. Default is 8080.
  -d DIR     Specifies the directory that the server will use to
             read/write requested files. Default is the current
             directory when launching the application.
"""
from docopt import docopt
from httpfs_server import run_server

def run():
    args = docopt(__doc__)  # parse arguments based on docstring above
    if(args.get("-p")):
        run_server(args.get("-v"), args.get("-d"), args.get("-p"))
    else:
        run_server(args.get("-v"), args.get("-d"))
