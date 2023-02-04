
# import codecs
# import re
# import os

# print("======file deleter======")
# print("======set file path======")

# # file_path = "C:/Users/new/Downloads/same-Copy.txt"
# file_path = input()

# print(file_path)
# none_obj = 0
# first = True
# with codecs.open(file_path, encoding='utf-8', mode = "r") as file:
#     for line in file:
#         out = re.search(r"([0-9]+)\;(C\:[a-zA-Z0-9а-яА-Я\ \_\.\,\\\/]+)\;([0-9]+)\;", line)
#         if out == None:
#             continue

#         if int(out.group(3)) >= 90:
            
#             first = not first
#             if not first:
#                 continue
#             if os.path.exists(out.group(2)):
#                 os.remove(out.group(2))
#                 print("removed : {} : {}%".format(out.group(1), out.group(2), out.group(3)), end = "\n")

import codecs
import re
import os

print("======file deleter======")
print("======set file path======")

file_path = input()

print("======add the minimal procente that you want to delete======\n(recomeneded min value is 95)")

min_procente = int(input())
print(min_procente)

print(file_path)
first = True
with codecs.open(file_path, encoding='utf-8', mode = "r") as file:
    for line in file:
        out = re.search(r"([0-9]+)\;(C\:[a-zA-Z0-9а-яА-Я\ \_\.\,\\]+)\;([0-9]+)\;", line)
        # print(out)
        if out == None:
            continue
        couple = out.group(1)
        path = out.group(2)
        procente = out.group(3)

        if int(procente) >= min_procente:
            
            first = not first
            if not first:
                continue
            if os.path.exists(path):
                # os.remove(path)
                print("removed {} : {} : {}%".format(couple, path, procente), end = "\n")

