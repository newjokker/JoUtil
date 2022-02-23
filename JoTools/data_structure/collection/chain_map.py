# -*- coding: utf-8  -*-
# -*- author: jokker -*-

from collections import ChainMap


baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}

print(list(ChainMap(adjustments, baseline)))

