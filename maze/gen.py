#!/usr/bin/env python
# -*- coding: utf-8 -*-

import struct

m = [
    [0, 2, 1, 0, 1, 0, 1, 1, 1, 3, 0, 1, 0, 3, 0, 1, 1, 0, 1, 1],
    [2, 1, 0, 1, 2, 2, 0, 0, 1, 2, 2, 2, 2, 0, 3, 0, 2, 2, 0, 0],
    [1, 2, 2, 0, 3, 2, 2, 2, 0, 3, 2, 1, 3, 2, 0, 3, 2, 1, 3, 1],
    [1, 3, 2, 1, 2, 3, 2, 2, 1, 3, 2, 2, 0, 3, 1, 3, 1, 2, 0, 0],
    [1, 1, 3, 0, 3, 0, 3, 1, 2, 0, 1, 3, 1, 1, 1, 1, 2, 2, 2, 0],
    [0, 1, 3, 1, 2, 2, 0, 1, 3, 2, 0, 2, 0, 2, 0, 3, 1, 2, 2, 1],
    [0, 2, 0, 1, 3, 2, 2, 1, 0, 3, 2, 1, 3, 2, 1, 0, 2, 1, 1, 0],
    [3, 2, 1, 2, 1, 2, 2, 0, 0, 3, 1, 1, 2, 2, 2, 2, 1, 2, 2, 0],
    [0, 1, 1, 3, 0, 2, 2, 2, 1, 1, 1, 2, 2, 1, 0, 3, 2, 1, 2, 0],
    [0, 0, 0, 0, 2, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0]
]

f = open('qqq', 'wb')
f.write(struct.pack('i', len(m[0])))
f.write(struct.pack('i', len(m)))

for y in range(len(m)):
    for x in range(len(m[0])):
        f.write(struct.pack('c', str(unichr(m[y][x]))))

f.close()
