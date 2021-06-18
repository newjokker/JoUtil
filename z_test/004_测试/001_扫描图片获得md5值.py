# -*- coding: utf-8  -*-
# -*- author: jokker -*-


from JoTools.utils.HashlibUtil import HashLibUtil





img_dir = r"C:\Users\14271\Desktop\del\del_test"


HashLibUtil.leave_one(img_dir=img_dir, endswith=(".JPG", ".PNG", ".jpg", ".png"), del_log_path=r"C:\Users\14271\Desktop\del\del_test\del_log.txt")