import os
import re
from logger_init import logger
from HTTPException import HTTPException
import portalocker

# Perform GET on pathname
#path_from_request, server_working_directory, absolute_path
def get_file(path_from_request, verbose, server_working_directory):
    absolute_path, server_working_directory = get_absolute_path(server_working_directory, path_from_request)
    # Check if user has access to the file
    user_has_access(absolute_path, server_working_directory)

    if path_from_request == "/" or os.path.isdir(absolute_path):
        #return tree
        logger.info("Returning list of files in main directory: %s", absolute_path)
        return list_files(absolute_path)
    else:
        # Check if file exists
        file_exists(absolute_path)
        #return contents of file
        with portalocker.Lock(absolute_path, 'r') as content_file:
            logger.info("Returning content of file at %s", absolute_path)
            return content_file.read()

def post_file(path_from_request, file_content, verbose, server_working_directory, overwrite=True):
    absolute_path, server_working_directory = get_absolute_path(server_working_directory, path_from_request)

    # Check if user access is granted
    user_has_access(absolute_path, server_working_directory)
    # Check if pathname exists
    pathname_exists(absolute_path)
    # Check if pathname is not directory
    is_not_directory(absolute_path)

    # Check if overwrite or append
    if overwrite:
        editing_mode = 'w'
    else:
        editing_mode = 'a'

    # Edit file
    with open(absolute_path, editing_mode) as file:
        file.write(file_content)
        return file_content + "\n\r"
    file.closed

def get_absolute_path(server_working_directory, path_from_request):
    if(server_working_directory != "None"):
        # set the directory
        server_directory = server_working_directory
    else:
        # default is current directory
        server_directory = os.getcwd()
    return server_directory+path_from_request, server_directory

# Returns true if user has access, raises HTTPException(403) if access denied
def user_has_access(absolute_path, server_working_directory):
#   check if /files is a parent of file or directory, if true, True, else, exception
    real_pathname = str(os.path.realpath(absolute_path))
    if re.search(r"\A%s" % server_working_directory, real_pathname):
        return True
    else:
        raise HTTPException(403)

# Returns true if pathname exists, raises HTTPException(404) if it does not
def pathname_exists(absolute_path):
    file_parent = os.path.dirname(absolute_path)
    if os.path.isfile(absolute_path) or os.path.isdir(file_parent):
        return True
    else:
        raise HTTPException(404)

# Returns true is file with pathname exists, raises HTTPException(404) if not
def file_exists(absolute_path):
    if os.path.isfile(absolute_path):
        return True
    else:
        raise HTTPException(404)
def is_not_directory(absolute_path):
    if os.path.isdir(absolute_path):
        raise HTTPException(404)
    else:
        return True

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
