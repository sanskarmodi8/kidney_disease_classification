import os
import sys
import logging

# format of the logging message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# create logs folder if not exists 
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# set the config 
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# create an object of the logger
logger = logging.getLogger("kidneyDiseaseClassifierLogger")