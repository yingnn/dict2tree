# dict2tree

display dict object tree like, like shell command 'tree' shows.

## usage

In [1]: from dict2tree import dict2tree


In [2]: d = {'a': {'b': {'c': 'd'}}}


In [3]: dict2tree(d)

.
\__ a
    \__ b
        \__ c
            \__ d
