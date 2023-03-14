import logging
import inspect
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        print("LOGGER NAME:", loggerName)
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler("logfile_report.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s: %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
