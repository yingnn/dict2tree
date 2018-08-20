from __future__ import print_function
import json
import os
import sys
import argparse


k = 0
l = set()


def get_args():
    ap = argparse.ArgumentParser(description='display dict object as tree diagram')
    ap.add_argument('-d', '--demo', action="store_true", help='show demo')
    ap.add_argument('-j', '--json', help='json file or json string')
    return ap.parse_args()


def json2dict(s):
    if os.path.exists(s):
        with open(s) as f_:
            return json.load(f_)
    else:
        return json.loads(s)


def fmt_s(k, l, indent=4):
    s = ''
    for i in range(1, k):
        if i in l:
            s += '|' + (indent - 1) * ' '
        else:
            s += indent * ' '

    s += '\\' + (indent - 2) * '_' + ' %s'
    return s


def dict2tree(obj, root='root', indent=4):
    global k
    if k == 0:
        print(root)
    if not isinstance(obj, dict) and \
        not isinstance(obj, list):
        k += 1
        print(fmt_s(k, l, indent) % obj)
        k -= 1

    elif isinstance(obj, dict):
        k += 1
        if len(obj) > 1:
            l.add(k)
            ks = obj.keys()
            for i in ks[:-1]:
                print(fmt_s(k, l, indent) % i)
                dict2tree(obj[i], indent=indent)

            l.remove(k)
            print(fmt_s(k, l, indent) % ks[-1])
            dict2tree(obj[ks[-1]], indent=indent)
        else:
            for i in obj:
                print(fmt_s(k, l, indent) % i)
                dict2tree(obj[i], indent=indent)
        k -= 1

    elif isinstance(obj, list):
        for i in obj:
            dict2tree(i, indent=indent)


def main(root='root', indent=4):
    args = get_args()
    if args.demo:
        j = '{"a": {"b": {"c": "d", "e": "f"}}, "g": "h"}'
    if args.json is not None:
        j = args.json
    d = json2dict(j)
    dict2tree(d, root, indent)


if __name__ == '__main__':
    main()
