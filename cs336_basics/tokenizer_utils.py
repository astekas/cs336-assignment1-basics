import regex as re


def join_bytes(tup):
    l = len(tup)
    if l == 0:
        return None
    else:
        nb = tup[0]
        for i in range(1, l):
            nb += tup[i]
        return nb


def upd_dic(k, v, dic):
    if k in dic.keys():
        dic[k] += v
    else:
        dic[k] = v


def pretokenize(s):
    PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""
    out_dic = {}
    for k in re.finditer(PAT, s):
        upd_dic(k.group(0), 1, out_dic)
    return out_dic


def pretokenize_mult(input_path, special_tokens, bounds):
    with open(input_path, 'rb') as file:
        PAT = r"""'(?:[sdmt]|ll|ve|re)| ?\p{L}+| ?\p{N}+| ?[^\s\p{L}\p{N}]+|\s+(?!\S)|\s+"""

        start, end = bounds
        file.seek(start)
        chunk = file.read(end - start).decode("utf-8", errors="ignore")

    str_split = re.split('|'.join([re.escape(st) for st in special_tokens]), chunk)
    out_dic = {}
    for s in str_split:
        for k in re.finditer(PAT, s):
            upd_dic(k.group(0), 1, out_dic)
    return out_dic