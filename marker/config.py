import os


# MARKER DIRS
MARKER_DATA_HOME = os.getenv('MARKER_DATA_HOME')
MARKER_HOME = os.getenv('MARKER_HOME')
MARKER_TLDR_DIR = os.path.join(os.getenv('MARKER_HOME'), 'tldr')

# MARKER FILES
USER_COMMAND_TXT_FILE = 'user_commands.txt'
COMMON_TXT_FILE = 'common.txt'

# OTHER
USE_OTHER_MARK_FILES = True