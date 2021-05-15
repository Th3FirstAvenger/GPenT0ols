
from termcolor import colored


def highlight(text, color='yellow'):
    if color == 'yellow':
        return u'{}'.format(colored(text, 'yellow', attrs=['bold']))
    elif color == 'red':
        return u'{}'.format(colored(text, 'red', attrs=['bold']))
