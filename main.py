import pandas as pd
import sys
from driver import *
from fence_driver import *
from s3_filedownload_trash import *

BUCKET_NAME=sys.argv[1]
FILE_NAME=sys.argv[2]

s3_down(FILE_NAME, BUCKET_NAME)

move_file_to_trash(BUCKET_NAME, FILE_NAME)

CSV= f'/home/eminds/em-dt-backend/FenceGraph/SG_Fence_Core/CSV_s3/{FILE_NAME}'
dataframe = pd.read_csv(CSV)
print("shape: ", dataframe.shape)

p1 = Process(target=rules_engine, args=(dataframe,))
p2 = Process(target=stats_engine, args=(dataframe,))
p1.start()
p2.start()
p1.join()
p2.join()


fence_engine(dataframe)
