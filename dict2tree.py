from __future__ import print_function
import json
import os


k = 0
l = set()


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
            if indent == 2:
                s += '| '
            elif indent == 3:
                s += '|  '
            else:
                s += '|   '
        else:
            if indent == 2:
                s += 2 * ' '
            elif indent == 3:
                s += 3 * ' '
            else:
                s += 4 * ' '
    if indent == 2:
        s += '\ %s'
    elif indent == 3:
        s += '\_ %s'
    else:
        s += '\__ %s'

    return s


def dict2tree(obj, root='.', indent=4):
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


if __name__ == '__main__':
    j = '{"a": {"b": {"c": "d"}}}'
    d = json2dict(j)
    dict2tree(d, 'root', 3)
