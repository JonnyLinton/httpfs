import os
from HTTPException import HTTPException

SERVER_DIRECTORY = os.getcwd() + "/files"

# returns either directory tree or contents of file
def get_file(pathname):
    # Check if user has access to the file
    user_has_access(pathname)
    # Check if file exists
    file_exists(pathname)

    if(pathname == "/"):
        #return tree
        return list_files(SERVER_DIRECTORY)
    else:
        #return contents of file
        with open(SERVER_DIRECTORY+pathname, 'r') as content_file:
            return content_file.read()

def post_file(pathname, file_content, overwrite=True):
    # Check if user access is granted
    user_has_access(pathname)
    # Check if pathname exists
    pathname_exists(pathname)

    # Check if overwrite or append
    if overwrite:
        editing_mode = 'w'
    else:
        editing_mode = 'a'

    # Edit file
    with open(pathname, editing_mode) as file:
        file.write(file_content)
    file.closed
    return True

def user_has_access(pathname):
    # returns true if user has access, raises HTTPException(403) if access denied
    return True

def pathname_exists(pathname):
    # returns true if pathname exists, raises HTTPException(404) if it does not
    return True

def file_exists(pathname):
    if os.path.isfile(pathname):
        return True
    else:
        raise HTTPException(404)

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
