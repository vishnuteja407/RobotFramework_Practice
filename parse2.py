# with open("Testdata/common-service-cewa-Voice.csv", "r") as voice_devices:
#     with open("Testdata/common-service-cewa-VoiceData.csv", "r") as data_voice_devices:

# import pandas as pd
# # voice_devices = pd.read_csv("Testdata/common-service-cewa-Voice.csv", names=["Voice Devices"]).to_dict()
# voice_devices = pd.read_csv("Testdata/common-service-cewa-Voice.csv").to_dict()
# print(voice_devices)
# data_voice_devices = pd.read_csv("Testdata/common-service-cewa-VoiceData.csv").to_dict()
# print(data_voice_devices)
#
# # with open("Testdata/combined-devices.csv", 'w') as combined_data:
# for voice_device in voice_devices['Hostname']:
#     for data_voice_device in data_voice_devices['Hostname']:
#         if voice_devices['Hostname'][voice_device] == data_voice_devices['Hostname'][data_voice_device]:
#             print(voice_devices['Hostname'][voice_device])

# with open("Testdata/common-service-cewa-Voice.csv", "r") as voice_devices:
#     with open("Testdata/common-service-cewa-VoiceData.csv", "r") as data_voice_devices:
#         voice_devices = [x.replace('\n', '').replace("\ufeff",'') for x in voice_devices.readlines()]
#         data_voice_devices = [x.replace('\n', '').replace("\ufeff",'') for x in data_voice_devices.readlines()]
#         devicenames = list([voice_device for voice_device in voice_devices if voice_device not in data_voice_devices ])
#         with open('new_file.xlsx', 'w') as write_data:


# import csv
# with open("Testdata/common-service-cewa-Voice.csv", "r") as csv_data:
#     data = csv.reader(csv_data)
#     for row in data:
#         print(row)

# import pandas
#
# def find_cell(csv_file, header, devicename):
#     data = pandas.read_excel(csv_file, sheet_name='common-service-cewa-Voice')
#     print(data)
#     columns = [column for column in data.columns]
#     print(columns)
#     if header == columns[0]:
#         column_cell = 'A'
#     elif header == columns[1]:
#         column_cell = 'B'
#     # total_rows = len(data.axes[0])  # ===> Axes of 0 is for a row
#     # total_cols = len(data.axes[1])
#     values = list(data[data[header]==devicename].index.values)
#     positions = []
#     for value in values:
#         positions.append(column_cell+str(value+2))
#     return positions
#
#
#
# position_array = find_cell('Testdata/common-service-cewa-Voice.xls', 'BLC', 'SC1-023')
# print(position_array)
#
# import openpyxl
# from openpyxl.styles import PatternFill
# wb = openpyxl.load_workbook("Testdata/common-service-cewa-Voice.xltm")
# ws = wb['common-service-cewa-Voice'] #Name of the working sheet
# fill_cell1 = PatternFill(patternType='solid',
#                            fgColor='FC2C03')
# # fill_cell2 = PatternFill(patternType='solid',
# #                            fgColor='03FCF4')
# # fill_cell3 = PatternFill(patternType='solid',
# #                            fgColor='35FC03')
# # fill_cell4 = PatternFill(patternType='solid',
# #                            fgColor='FCBA03')
# for cell in position_array:
#     print(cell)
#     ws[cell].fill = fill_cell1
# # ws['B3'].fill = fill_cell2
# # ws['B4'].fill = fill_cell3
# # ws['B5'].fill = fill_cell4
# wb.save("Testdata/common-service-cewa-Voice.xltm")


# fan_status_list = [{'Status': u'', 'MinorThres': u'', 'CurTemp': u'', 'FanModel': u'NXA-FAN-30CFM-F ', 'PS': u'', 'TempStatus': u'', 'ActualOutput': u'', 'Direction': u'back-to-front', 'FanStatus': u' Ok ', 'Hw': u'--', 'Fan': u'Fan1(sys_fan1)', 'MajorThresh': u'', 'Model': u'', 'ActualInput': u'', 'TotalCapacity': u'', 'Module': u'', 'Sensor': u''}, {'Status': u'', 'MinorThres': u'', 'CurTemp': u'', 'FanModel': u'NXA-FAN-30CFM-F ', 'PS': u'', 'TempStatus': u'', 'ActualOutput': u'', 'Direction': u'back-to-front', 'FanStatus': u' Ok ', 'Hw': u'--', 'Fan': u'Fan2(sys_fan2)', 'MajorThresh': u'', 'Model': u'', 'ActualInput': u'', 'TotalCapacity': u'', 'Module': u'', 'Sensor': u''}, {'Status': u'', 'MinorThres': u'', 'CurTemp': u'', 'FanModel': u'NXA-FAN-30CFM-F ', 'PS': u'', 'TempStatus': u'', 'ActualOutput': u'', 'Direction': u'back-to-front', 'FanStatus': u' Ok ', 'Hw': u'--', 'Fan': u'Fan3(sys_fan3)', 'MajorThresh': u'', 'Model': u'', 'ActualInput': u'', 'TotalCapacity': u'', 'Module': u'', 'Sensor': u''}, {'Status': u'', 'MinorThres': u'', 'CurTemp': u'', 'FanModel': u'NXA-FAN-30CFM-F ', 'PS': u'', 'TempStatus': u'', 'ActualOutput': u'', 'Direction': u'back-to-front', 'FanStatus': u' Ok ', 'Hw': u'--', 'Fan': u'Fan4(sys_fan4)', 'MajorThresh': u'', 'Model': u'', 'ActualInput': u'', 'TotalCapacity': u'', 'Module': u'', 'Sensor': u''}, {'Status': u'', 'MinorThres': u'', 'CurTemp': u'', 'FanModel': u'  ', 'PS': u'', 'TempStatus': u'', 'ActualOutput': u'', 'Direction': u'none', 'FanStatus': u'None', 'Hw': u'--', 'Fan': u'Fan_in_PS1', 'MajorThresh': u'', 'Model': u'', 'ActualInput': u'', 'TotalCapacity': u'', 'Module': u'', 'Sensor': u''}, {'Status': u'', 'MinorThres': u'', 'CurTemp': u'', 'FanModel': u'-- ', 'PS': u'', 'TempStatus': u'', 'ActualOutput': u'', 'Direction': u'back-to-front', 'FanStatus': u' Ok', 'Hw': u'--', 'Fan': u'Fan_in_PS2', 'MajorThresh': u'', 'Model': u'', 'ActualInput': u'', 'TotalCapacity': u'', 'Module': u'', 'Sensor': u''}]
# fan_status_check = True
# for fan in fan_status_list:
#     sys_fan = fan.get("Fan")
#     sys_fan_status = fan.get("FanStatus").strip()
#     print(sys_fan_status)
#     fan_status_check = fan_status_check and sys_fan_status.lower() == "ok"

# list1 = [[{'deviceName': 'USNCCLTIJ10TDE0002LAB', 'exectionId': '63c0246a79d2b9003ddd406c'}, {'deviceName': 'USNCCLTIJ04TVE0001LAB', 'exectionId': '63c0246b79d2b9003ddd406d'}, {'deviceName': 'USCOENGFG01FIE1LAB', 'exectionId': '63c0246b79d2b9003ddd406e'}, {'deviceName': 'USAZGNDGD01FIE0001LAB', 'exectionId': '63c0246b79d2b9003ddd406f'}], [{'deviceName': 'USNCCLTIJ10TDE0002LAB', 'exectionId': '63c02485dbf1fd002ff66f0d'}, {'deviceName': 'USNCCLTIJ04TVE0001LAB', 'exectionId': '63c02485dbf1fd002ff66f0e'}, {'deviceName': 'USAZGNDGD01FIE0001LAB', 'exectionId': '63c02485dbf1fd002ff66f0f'}, {'deviceName': 'USCOENGFG01FIE1LAB', 'exectionId': '63c02485dbf1fd002ff66f10'}]]
# list1 = [{'deviceName': 'USNCCLTIJ04TVE0001LAB', 'id': '63c1112e9831b10141a27842'}, {'deviceName': 'USNCCLTIJ04TVE0001LAB', 'id': '63c1112e9831b10141a27842'}, {'deviceName': 'USNCCLTIJ04TVE0001LAB', 'id': '63c1112e9831b10141a27842'}, {'deviceName': 'USNCCLTIJ04TVE0001LAB', 'id': '63c1112e9831b10141a27842'}, {'deviceName': 'USCOENGFG01FIE1LAB', 'id': '63c111d29831b10141a27844'}, {'deviceName': 'USCOENGFG01FIE1LAB', 'id': '63c111d29831b10141a27844'}, {'deviceName': 'USCOENGFG01FIE1LAB', 'id': '63c111d29831b10141a27844'}, {'deviceName': 'USCOENGFG01FIE1LAB', 'id': '63c111d29831b10141a27844'}]
# list2 = list(map(lambda x: (x['deviceName'], {x['id']}), list1))
# print(list2)

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
# l = list([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])
#
# print(l)


# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#
# largest = arr[0]
# smallest = arr[0]
# largest2 = None
# Smallest2 = None
#
# for i in arr[1:]:
#     if i > largest:
#         largest2 = largest
#         largest = i
#     elif (largest2 is None or largest2 < i) and i < largest:
#         largest2 = i
#
# print(largest2)
# records = []
# names = []
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name, score])
#     scores = list(map(lambda x: x[1], records))
#     smallest = scores[0]
#     smallest2 = 0.0
#     for [name, score] in records:
#         if score < smallest:
#             smallest2 = smallest
#             smallest = score
#         elif smallest2 == 0.0 and score > smallest:
#             smallest2 = score
#     for [name, score] in records:
#         if score == smallest2:
#             names.append(name)
#     names.sort()
#     for name in names:
#         print(name)

# records = []
# names = []
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name, score])
#     scores = list(map(lambda x: x[1], records))
#     smallest_list = list(set(scores))
#     smallest_list.sort()
#     smallest2 = smallest_list[1]
#     for [name, score] in records:
#         if score == smallest2:
#             names.append(name)
#     names.sort()
#     for name in names:
#         print(name)

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#         print(student_marks)
#     query_name = input()
#     for key, value in student_marks.items():
#         print(key)
#         print(value)
#         if key == query_name:
#             avg = sum(value)/len(value)
#     print('{:.2f}'.format(avg))

# import operator
# from operator import itemgetter
# def person_lister(f):
#     def inner(people):
#         # people.sort(key=itemgetter(2))
#         people = sorted(people, key=lambda x: int(x[2]))
#         print(people)
#         return [f(person) for person in people]
#     return inner
#
# @person_lister
# def name_format(person):
#     return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]
#
# if __name__ == '__main__':
#     people = [input().split() for i in range(int(input()))]
#     print(*name_format(people), sep='\n')

# import numpy
# numpy.set_printoptions(legacy='1.13')
# import sys
#
# for line in sys.stdin:
#     if "\n" == line.rstrip():
#         break
#     print(type(line))
#     split_line = line.split(" ")
#     print(split_line)
#     data = list(map(float, split_line))
#     print(data)
#     my_array = numpy.array(data, dtype=numpy.float32)
#     print(numpy.floor(my_array))
#     print(numpy.ceil(my_array))
#     print(numpy.rint(my_array))

# import numpy as np
# np.set_printoptions(legacy='1.13')
# import sys
#
# array = list(map(float, input().split(" ")))
#
# print(np.floor(array), np.ceil(array), np.rint(array), sep="\n")

# import numpy
#
# my_array = numpy.array([[1,2,3],[4,5,6]])
# print(my_array)

# if __name__ == '__main__':
#     N = int(input())
#     list1 = []
#     list1.insert(0, 5)
#     list1.insert(1, 10)
#     list1.insert(0, 6)
#     print(list1)
#     list1.remove(6)
#     list1.append(9)
#     list1.append(1)
#     list1.sort()
#     print(list1)
#     list1.pop()
#     list1.reverse()
#     print(list1)

# if __name__ == '__main__':
#     N = int(input())
#     ops = [input() for n in range(N)]
#     l = []
#     for op in ops:
#         if op == 'print':
#             print(l)
#         else:
#             op, *args = op.split(" ")
#             args = list(map(int, args))
#             func = getattr(l, op)(*args)

# if __name__ == '__main__':
#     N = int(input())
#     l = []
#     for _ in range(N):
#         data = list(input().split(" "))
#         if len(data) > 1:
#             for i in range(1, len(data)):
#                 if data[i].isdigit():
#                     data[i] = int(data[i])
#         if data[0].lower() == 'insert':
#             l.insert(data[1], data[2])
#         if data[0].lower() == 'print':
#             print(l)
#         if data[0].lower() == 'remove':
#             l.remove(data[1])
#         if data[0].lower() == 'append':
#             l.append(data[1])
#         if data[0].lower() == 'pop':
#             l.pop()
#         if data[0].lower() == 'sort':
#             l.sort()
#         if data[0].lower() == 'reverse':
#             l.reverse()

# import builtins
# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     tuple_data = tuple(integer_list)
#     print(builtins.hash(tuple_data))

import re
for _ in range(int(input())):
    data = input()
    data1 = data.split(".")
    regex = re.compile(r"^[+-.]?.+")
    if len(data1) > 1 and data1[1] != "" and data1[1].isdigit():
        matched = regex.match(data)
        result = matched.group()
        if "+-" in result:
            print(False)
        else:
            print(True)
    else:
        print(False)




