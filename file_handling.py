import os
import re
from HTTPException import HTTPException

ACCESS_DIRECTORY = "/files"
SERVER_DIRECTORY = os.getcwd() + ACCESS_DIRECTORY

# Perform GET on pathname
def get_file(pathname):
    realPath = SERVER_DIRECTORY+pathname
    # print(realPath)
    # Check if user has access to the file
    # user_has_access(pathname)
    # Check if file exists
    file_exists(realPath)

    if(pathname == "/"):
        #return tree
        return list_files(SERVER_DIRECTORY)
    else:
        #return contents of file
        with open(realPath, 'r') as content_file:
            return content_file.read()

# Perform POST on inputted file
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

# Returns true if user has access, raises HTTPException(403) if access denied
def user_has_access(pathname): # not working properly
# python check if /files is a parent of file or directory, if true, True, else, exception
    real_pathname = str(os.path.realpath(pathname))
    if re.search(r"\A%s" % ACCESS_DIRECTORY, real_pathname):
        return True
    else:
        raise HTTPException(403)

# Returns true if pathname exists, raises HTTPException(404) if it does not
def pathname_exists(pathname):
    if os.path.isfile(pathname) or os.path.isdir(pathname):
        return True
    else:
        raise HTTPException(404)

# Returns true is file with pathname exists, raises HTTPException(404) if not
def file_exists(pathname):
    if os.path.isfile(pathname):
        return True
    else:
        raise HTTPException(404)

# Prints complete directory tree for path
def list_files(startpath):
    tree = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree += '{}{}/'.format(indent, os.path.basename(root)) + "\n"
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            tree += '{}{}'.format(subindent, f) + "\n"
    return tree
