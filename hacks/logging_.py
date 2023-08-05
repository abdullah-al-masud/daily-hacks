import logging
import os
import datetime



DEFAULT_LOG_FORMAT = '%(asctime)s - %(pathname)s - %(levelname)s - %(message)s'


def set_logging(
        log_dir=None,
        filename=None,
        log_format=None,
        log_level=logging.INFO,
        allow_print=False,
        print_level=logging.INFO,
        include_curtime=False
    ):
    """
    This function sets the logging definitions in a very easy way. 
    """
    
    if log_dir is None:
        log_dir = '.'

    if filename is None:
        filename = 'logfile%s.log'%current
    if log_format is None:
        log_format = DEFAULT_LOG_FORMAT

    if include_curtime:
        current = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        current = '-' + current
    else:
        current = ''

    if not os.path.isdir(log_dir):
        os.makedirs(log_dir)

    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    if allow_print:
        logging.root.handlers = []
        logging.basicConfig(filename=os.path.join(log_dir, filename), filemode='w', level=log_level,
                        format=log_format, datefmt='%Y-%m-%d %H:%M:%S')
        printer = logging.StreamHandler()
        printer.setLevel(print_level)
        logging.getLogger("").addHandler(printer)
    else:
        logging.basicConfig(filename=os.path.join(log_dir, filename), filemode='w', level=log_level,
                        format=log_format, datefmt='%Y-%m-%d %H:%M:%S')
