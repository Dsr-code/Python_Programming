'''Creating a Virtual Environment in python helps to handle the control of the program with the specific version of thepackages installed in the PC. '''

# Example
'''Suppose you are working in a project with pandas __version__ 1.0.2 and you send your program to a friend having pandas __version__ 1.0.1 , so the code will not be compatibble with the version of the package installed and he has to delete the pandas version or update the version. So to solve this problem He can create a virtual environment of the python installed with the required packages and run my code by activating the virtual environment and start the code and ater he is done he can deactivate the VrEn and return back to the global python in his PC'''

# to install a specific version of a module we can use
''' pip install module==version'''

# Setting the virtual environment


# To make a Virtual Environment

# Create a folder and type
'''python -m venv <folder_name>'''

# Activating the venv python 

# through powershell
'''<venv>\Scripts\Activate.ps1'''
# through cmd
'''<venv>\Scripts\Activate.bat'''

# this enables the venv python environment and to deactivate it type 
'''deactivate'''

# you can provide the required modules to run the program by applying the command
'''pip freeze > requirements.txt'''

# to install the packages 
'''pip install -r requirements.txt'''

# you can also type "pip freeze" to see the module installed in that environment