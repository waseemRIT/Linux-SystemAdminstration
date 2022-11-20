def does_exist(target):
    """
    Function to check if File Exists in the System
    Reads All files in the system under Home directory and the subdirectory
    Such that it would check all files within the system to determine if it's valid to create a symbolic link for it
    """
    for dirPath, dirNames, files in os.walk(home):
        for file in files:
            if file == target:
                return True
    return False