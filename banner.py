"""
    Creating a logo using PyFiglet
    Felix Kiprop
"""
from colorama import Style
from pyfiglet import Figlet

def display_banner():
    """Function used to call pyfiglet to create a 'Furl' text"""
    custom_fig = Figlet(font='slant')
    print(custom_fig.renderText('Url Status Checker') + Style.RESET_ALL)
    print("\tv1.0.0")
    print("\tFelix Kiprop\n\n")
