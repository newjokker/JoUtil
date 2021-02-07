# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.txkjRes.detectionResult import DeteRes


a = DeteRes()
a.add_obj()

a.do_nms_in_assign_tags(['Lm', 'KG', 'K'], 0.1)

a.get_fzc_format()