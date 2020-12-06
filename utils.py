import os
import platform
import pathlib

CLS_CMD = 'clear' if platform.system() == 'Linux' else 'cls'


def cls():
    """Limpa o console (funciona em windows e linux)"""
    os.system(CLS_CMD)


def download_folder():
    """Identifica a pasta Downloads do usuário (windows e linux)"""
    return os.path.join(pathlib.Path().home(), 'Downloads')
