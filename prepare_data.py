print("Do not run, is slow and runs MPS out of memory.")
exit()
from utils import *

download_data(data_folder=os.path.expanduser("~/torch_datasets/transformer_data"))

prepare_data(data_folder=os.path.expanduser("~/torch_datasets/transformer_data"),
             euro_parl=True,
             common_crawl=True,
             news_commentary=True,
             min_length=3,
             max_length=150,
             max_length_ratio=2.,
             retain_case=True)
