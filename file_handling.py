import os
from HTTPException import HTTPException

SERVER_DIRECTORY = os.getcwd() + "/files"

# Perform GET on pathname
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
def user_has_access(pathname):
    return True

# Returns true if pathname exists, raises HTTPException(404) if it does not
def pathname_exists(pathname):
    return True

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
