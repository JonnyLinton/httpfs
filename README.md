# httpfs

httpfs is a simple file server.

# Installation
While in the directory of the repo:
`pip install -e .` (runs setup.py, installs `docopt`)

# Usage
httpfs [-v] [-p PORT] [-d PATH-TO-DIR]<br/>
- `-v`   Prints debugging messages.<br/>
- `-p` Specifies the port number that the server will listen and serve at. Default is 8080. <br/>
- `-d`   Specifies the directory that the server will use to read/write requested files. Default is the current directory when launching the application. <br/>

## Example Usage
`httpfs -v -p 8080 -d "/Users/user/Documents/files"`
