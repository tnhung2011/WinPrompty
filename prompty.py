import platform
from sys import exit
from os import system
from sys.stdin import isatty
from os.path import dirname, realpath
from colorama import init, Fore, Back
from tkinter.messagebox import showerror


if platform.system() is 'Windows':
    if platform.release >= '6':
        init()
        if not isatty:
            system("title WinPrompty")
        system("cmd /Q /D /C @echo off^&set ResetFore={Fore.RESET}^&set RedFore={Fore.RED}^&set GreenFore={Fore.GREEN}^&set YellowFore={Fore.YELLOW}^&set BlueFore={Fore.BLUE}^&set MagentaFore={Fore.MAGENTA}^&set CyanFore={Fore.CYAN}^&set WhiteFore={Fore.WHITE}^&^&set ResetBack={Back.RESET}^&set RedBack={Back.RED}^&set GreenBack={Back.GREEN}^&set YellowBack={Back.YELLOW}^&set BlueBack={Back.BLUE}^&set MagentaBack={Back.MAGENTA}^&set CyanBack={Back.CYAN}^&set WhiteBack={Back.WHITE}^&doskey clear=cls^&doskey true=prompt %GreenFore%$$:$F$S%ResetFore%^&doskey false=prompt %RedFore%$$:$C$S%ResetFore%^&doskey true/false=prompt $$:S$S^&doskey false/true=prompt $$:S$S^&prompt $$:$F$S^&@echo on")
    else:
        exit(showerror("WinPrompty", "This version of Windows is not supported."))
else:
    exit(showerror("WinPrompty", "This operating system is not supported."))
