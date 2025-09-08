import json
import gzip
import os
import jsonlines

# 单选题读取
def read_choice(input_file_path: str):
    # 打开并读取JSON文件
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 填空题读取
def read_fill(input_file_path: str):
    # 打开并读取JSON文件
    with open(input_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_jsonl(filename, data, append: bool = False):
    """
    Writes an iterable of dictionaries to jsonl
    """
    if append:
        mode = 'a'
    else:
        mode = 'w'
        # filename = os.path.expanduser(filename)
    if filename.endswith(".gz"):
        with open(filename, mode) as fp:
            with gzip.GzipFile(fileobj=fp, mode='wb') as gzfp:
                for x in data:
                    gzfp.write((json.dumps(x) + "\n").encode('utf-8'))
    else:
        with jsonlines.open(filename, mode) as fp:
            for x in data:
                fp.write(x)
