"""
Facade Pattern: Provide uniform interface to the users.
User can use it to communicate with multiple subsystems.

Facade pattern hides the complexities of the system and provides
an interface to the client using which the client can access the system.
This type of design pattern comes under structural pattern as
this pattern adds an interface to existing system to hide its complexities.
"""


class PythonConvertor:
    """
    Python Convertor converts any file to python file by renaming.
    Doesn't contain main logic, it is just sample class.
    """
    def __init__(self):
        self.name = "Python-Convertor"

    def rename(self, filename):
        """ Rename the file
            Change extension to .py
        Args:
            filename (str): file name
        Returns:
            str: renamed file name
        """
        filename_parts = filename.split(".")
        filename_parts[-1] = "py"
        renamed_filename = ".".join(filename_parts)
        return renamed_filename


class JavaConvertor:
    """
    Java Convertor converts any file to java file by renaming.
    Doesn't contain main logic, it is just sample class.
    """
    def __init__(self):
        self.name = "Java-Convertor"

    def rename(self, filename):
        """ Rename the file
            Change extension to .php
        Args:
            filename (str): file name
        Returns:
            str: renamed file name
        """
        filename_parts = filename.split(".")
        filename_parts[-1] = "java"
        renamed_filename = ".".join(filename_parts)
        return renamed_filename


class PHPConvertor:
    """
    PHP Convertor converts any file to php file by renaming.
    Doesn't contain main logic, it is just sample class.
    """
    def __init__(self):
        self.name = "PHP-Convertor"

    def rename(self, filename):
        """ Rename the file
            Change extension to .php
        Args:
            filename (str): file name
        Returns:
            str: renamed file name
        """
        filename_parts = filename.split(".")
        filename_parts[-1] = "php"
        renamed_filename = ".".join(filename_parts)
        return renamed_filename


class FileConvertorFacade:
    """
    It is actually not convertor it just rename filename

    it uses other subsystems/classes and provide features to the user.
    """
    def convert_file(self, filename, target_extension):
        if target_extension in ["py", "php", "java"]:
            convertor = None
            if target_extension == "py":
                convertor = PythonConvertor()
            elif target_extension == "java":
                convertor = JavaConvertor()
            elif target_extension == "php":
                convertor = PHPConvertor()
            renamed_filename = convertor.rename(filename)
            print("Converted file name : ", renamed_filename)
        else:
            print("Invalid Extension selected!")
            return 0


if __name__ == "__main__":

    file_convertor = FileConvertorFacade()

    input_file = input("Enter input file name : ")
    target_extension = input("File will be converted into which extension: ")
    file_convertor.convert_file(input_file, target_extension)
