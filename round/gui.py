import os
import asyncio
import itertools
import shutil
import threading
import gc

import logging



""" TODO: LET'S CHANGE THIS LATER TO ARGS """
cuda_device=None
deterministic=False
""" TODO: LET'S CHANGE THIS LATER TO ARGS """

if os.name == "nt":
    logging.getLogger("xformers").addFilter(lambda record: 'A matching Triton is not available' not in record.getMessage())

if cuda_device is not None:
    os.environ['CUDA_VISIBLE_DEVICES'] = str(cuda_device) # cuda device setting
    logging.info("Set cuda device to: {}".format(cuda_device))

if deterministic:
    if 'CUBLAS_WORKSPACE_CONFIG' not in os.environ:
        os.environ['CUBLAS_WORKSPACE_CONFIG'] = ":4096:8" # deterministism & reproducibility for Basic Linear Algebra Subprograms

import round.cuda_malloc as cuda_malloc


""" TODO: LET'S cHANGE THIS LATER TO ARGS """
windows_standalone_build = False
""" TODO: LET'S cHANGE THIS LATER TO ARGS """

if windows_standalone_build:
    try:
        import round.windows.fix_torch
    except:
        pass






