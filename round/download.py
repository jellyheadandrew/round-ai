import gdown

def download_dataset_from_gdrive(
    url: str, # google drive url that contains dataset. The drive must be accessible to anyone.
    output: str = ".",
    cookie_file: str=None, # must be provided for long-term download via gdown
    resume: bool = False,
    quiet: bool = False # whether to show progress or not   
    ):
    
    gdown.download_folder(
        url=url, 
        quiet=quiet, 
        output=output,
        resume=resume,    
    )
    
def download_dataset():
    pass