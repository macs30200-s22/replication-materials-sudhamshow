import json, pickle, lzma
from os import listdir
import pandas as pd
import numpy as np
from tqdm import tqdm

file_dict = {}
reddit_data = {}
file_set = set()


def count_mod(path_to_file_dir: str):
    temp = []
    for file in tqdm(sorted(listdir(path_to_file_dir))):
        if file.endswith('xz'):
            if file.split('.')[0] in file_set or file.startswith('.'):
                continue
            else:
                file_set.add(file.split('.')[0])
            # print(file)
            with lzma.open(path_to_file_dir + file) as f:
                # file_dict.setdefault(file.split('.')[0].split('_')[1], list()).append(file)
                lines = f.readlines()
                for line in lines:
                    temp.append(json.loads(line))
                dataDF = pd.DataFrame(temp)
                with open("path_to_output_file_neg_count",'a+') as f:
                    f.write(f"{file}, {len(dataDF[(dataDF['body'] == '[removed]') & (dataDF['score'] < -50)])} \n")
                with open("path_to_output_file_pos_count", 'a+') as f:
                    f.write(f"{file}, {len(dataDF[(dataDF['body'] == '[removed]') & (dataDF['score'] > 100)])} \n")
                temp = []

        else:
            if file.split('.')[0] in file_set or file.startswith('.'):
                continue
            else:
                file_set.add(file.split('.')[0])
            # print(file)
            with open(path_to_file_dir + file) as f:
                lines = f.readlines()
                for line in lines:
                    temp.append(json.loads(line))
                dataDF = pd.DataFrame(temp)
                with open("path_to_output_file_neg_count", 'a+') as f:
                    f.write(f"{file}, {len(dataDF[(dataDF['body'] == '[removed]') & (dataDF['score'] < -50)])} \n")
                with open("path_to_output_file_pos_count", 'a+') as f:
                    f.write(f"{file}, {len(dataDF[(dataDF['body'] == '[removed]') & (dataDF['score'] > 100)])} \n")
                temp = []
