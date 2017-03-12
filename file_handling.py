import os

SERVER_DIRECTORY = os.getcwd() + "/files"

# returns either directory tree or contents of file
def get_file(pathname):
    if(not isvalid(pathname)):
        #if the pathname is not valid, fail
        raise Exception("Invalid path!");

    if(pathname == "/"):
        #return tree
        return os.listdir(SERVER_DIRECTORY)
    else:
        #return contents of file
        with open(SERVER_DIRECTORY+pathname, 'r') as content_file:
            return content_file.read()


def post_file(pathname, file_content, overwrite=True):
    # Louis-Olivier
    # returns true or false
    # check if the valid pathname
    if not isvalid(pathname):
        return "Invalid path"
    # check if overwrite or append
    if overwrite:
        editing_mode = 'w'
    else:
        editing_mode = 'a'
    # edit file
    with open(pathname, editing_mode) as file:
        file.write(file_content)
    file.closed
    return True

def isvalid(pathname):
    # Louis-Olivier
    # returns true if access to directory is allowed
    return True
