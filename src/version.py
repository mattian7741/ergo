"""Summary.

Attributes:
    VERSION (str): Description

"""
import subprocess
import sys

VERSION = '0.3.30-alpha'


def get_version() -> str:
    """Summary.

    Returns:
        str: Description

    """
    return VERSION


# wtc && match => ok
# wtc && incr => not ok
# changes && incr => ok
# changes && match => not ok
if __name__ == '__main__':
    ver: str = get_version()
    tag: str = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8')
    status: str = subprocess.check_output(['git', 'status']).decode('utf-8')
    try:
        if tag.index(ver) == 0 and 'working tree clean' not in status:  # if version hasn't changed
            print('Version must be incremented with changes to codebase')
            sys.exit(1)
        else:
            # print('not status')
            # sys.exit(0)
            print(get_version())
    except ValueError:
        print(get_version())
