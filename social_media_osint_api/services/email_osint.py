# Importing required module
import subprocess
import sys
from haveibeenpwnd import check_email

infoga_path = 'D:\Git\emailosint'
# Include this line if your script is not in the sherlock folder
sys.path.insert(0, infoga_path)

# need to write code to use infoga library
from emailosint import infoga


def search_username_and_store(username):
    maigret_args = [
        'emailosint.py',
        username
    ]
    # osint_data = maigret_main(maigret_args)
    completed_process = subprocess.run(maigret_args, capture_output=True, text=True)

    return completed_process


if __name__ == '__main__':
    # search_username_and_store("eeee")
    sys.argv = ["aa", "-i", "adds0072004@hotmail.com", "-v", 3]
    # infoga().main()
    check_email("a@hotmail.com")
