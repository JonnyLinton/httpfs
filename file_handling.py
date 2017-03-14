import os
import re
from HTTPException import HTTPException

ACCESS_DIRECTORY = "/files"
SERVER_DIRECTORY = os.getcwd() + ACCESS_DIRECTORY

# Perform GET on pathname
def get_file(pathname, verbose, directory):
    print("Inside get_file, directory: " +directory)
    realPath, server_directory = resolveRealPath(directory, pathname)
    # Check if user has access to the file
    user_has_access(realPath, server_directory)

    if(pathname == "/"):
        #return tree
        return list_files(server_directory)
    else:
        # Check if file exists
        file_exists(realPath)
        #return contents of file
        with open(realPath, 'r') as content_file:
            return content_file.read()

# Perform POST on inputted file
def post_file(pathname, file_content, verbose, directory, overwrite=True):
    realPath = resolveRealPath(directory, pathname)

    # Check if user access is granted
    user_has_access(realPath)
    # Check if pathname exists
    pathname_exists(realPath)

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

def resolveRealPath(directory, pathname):
    if(directory != "None"):
        # set the directory
        print("Inside resolveRealPath, assigning to value")
        server_directory = directory
    else:
        # default is current directory
        print("Inside resolveRealPath, assigning current directory")
        server_directory = os.getcwd()
    return server_directory+pathname, server_directory

# Returns true if user has access, raises HTTPException(403) if access denied
def user_has_access(pathname, directory): # not working properly
# python check if /files is a parent of file or directory, if true, True, else, exception
    print("Inside user_has_access, pathname: " +pathname +"  directory: " +directory)
    real_pathname = str(os.path.realpath(pathname))
    if re.search(r"\A%s" % directory, real_pathname):
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
