import logging

logger = logging.getLogger(__name__)

class Context:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        logging.info(name + ": __enter__() is called")

    def __exit__(self, type, value, traceback):
        logging.info(name
                     + ": type=" + type + "\n"
                     + "; value=" + value + "\n"
                     + "; traceback=" + traceback)


with Context.new("test1"):
    
    
