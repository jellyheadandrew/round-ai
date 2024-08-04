import os
import shutil



""" TODO """

""" This script checks whether execution is successful for 'prestartup_script.py' under custom nodes folder. However, after implementation, check if necessary."""
from round.generate_script import import_generated_module

# check comfyui main.py -> execute_prestartup_script.py
def execute_prestartup_script():
    def execute_script(script_path):
        try:
            import_generated_module(script_path)
            return True
        except Exception as e:
            print(f"Failed to execute startup-script: {script_path} / {e}")
        return False
    
    """ IS THIS NEEDED """
    # if disable_all_custom_nodes:
    #     return    
    """ IS THIS NEEDED """

""" This script checks whether execution is successful for 'prestartup_script.py' under custom nodes folder. However, after implementation, check if necessary."""


""" TODO """



class FilePathHandler:
    def __init__(self, dataset_pth):
        super().__init__()
        
        self.dataset_pth = dataset_pth
        
        # temp dir
        self.set_temp_directory() 
        self.cleanup_temp()
        

    ## temporary directory for saving     
    def set_temp_directory(self, temp_dir=None):
        # default
        if temp_dir is None:
            self.temp_dir = f"{self.dataset_pth}/.round/temp"
        else:
            self.temp_dir = temp_dir

    def get_temp_directory(self):
        return self.temp_dir

    def cleanup_temp(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir, ignore_errors=True)
            