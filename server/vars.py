SERVER_PATH = '/Users/Artem/Desktop/school_server/server'
#SERVER_PATH = '/home/Torrentov/file_server'

PATH = SERVER_PATH + '/files/'
TMP_PATH = PATH + 'tmp/'
FILE_PATH = PATH + 'static/needed_files'

#DEFAULT_SITE = 'http://torrentov.pythonanywhere.com/files'
DEFAULT_SITE = 'http://127.0.0.1:8000/files'
SITE = DEFAULT_SITE + '?folder='
SITE_UPLOAD = DEFAULT_SITE + '/upload'
SITE_DELETE_FOLDER = DEFAULT_SITE + '/delete_folder'
SITE_DELETE_FILE = DEFAULT_SITE + '/delete_file'
SITE_CREATE_FOLDER = DEFAULT_SITE + '/mkdir'
FILE_DELETE = SITE_DELETE_FILE + '/file_remove?delete='
FOLDER_DELETE = SITE_DELETE_FOLDER + '/folder_remove?delete='

#FONT_PATH = "~/.fonts/8277.ttf"
FONT_PATH = "/Users/Artem/Downloads/8277.ttf"