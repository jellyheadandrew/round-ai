import importlib
from typing import Union
from pathlib import Path
import os

def import_generated_module(filename: Union[str, Path]):
    assert os.path.exists(filename)
    module_name = os.path.splitext(filename)[0]

    spec = importlib.util.spec_from_file_location(module_name, filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module