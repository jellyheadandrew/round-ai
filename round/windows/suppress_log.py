import logging

logging.getLogger("xformers").addFilter(lambda record: 'A matching Triton is not available' not in record.getMessage())