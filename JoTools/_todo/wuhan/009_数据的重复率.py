
from JoTools.utils.JsonUtil import JsonUtil


# 自重复，与其他时期的数据的重复


wh = JsonUtil.load_data_from_json_file(r"C:\Users\jokker\Desktop\md5_file\md5_wuhan.json")["md5_list"]
print(len(wh))
wh = set(wh)
print(len(wh))

print('-'*30)

old_07 = JsonUtil.load_data_from_json_file(r"C:\Users\jokker\Desktop\md5_file\md5_07.json")["md5_list"]
print(len(old_07))
old_07 = set(old_07)
print(len(old_07))

print('-'*30)

old_11 = JsonUtil.load_data_from_json_file(r"C:\Users\jokker\Desktop\md5_file\md5_11.json")["md5_list"]
print(len(old_11))
old_11 = set(old_11)
print(len(old_11))

print('-'*30)

# -----------------------------------------------

print(len(old_07.intersection(old_11)))
print(len(old_07.intersection(wh)))
print(len(old_11.intersection(wh)))




