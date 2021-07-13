from JoTools.utils.HashlibUtil import HashLibUtil
from JoTools.utils.FileOperationUtil import FileOperationUtil

list_1 = FileOperationUtil.re_all_file(r"D:\集中培育-11月样本\金具\保护金具\防振锤", lambda x:str(x).endswith(('.jpg', '.JPG')))
list_2 = FileOperationUtil.re_all_file(r"D:\算法培育-7月样本\金具\保护金具\防振锤", lambda x:str(x).endswith(('.jpg', '.JPG')))

print(len(list_1))
print(len(list_2))
list_1.extend(list_2)


res = HashLibUtil.duplicate_checking(list_1)

print(len(res))
