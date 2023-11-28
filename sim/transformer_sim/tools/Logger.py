import logging, os


def NetworkLogger(name):

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not os.path.exists('result'): os.makedirs('result')
    fpath = "result/%s.network.log" % name

    if os.path.exists(fpath):
        os.remove(fpath)

    fh = logging.FileHandler(fpath)
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(levelname)s] %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger