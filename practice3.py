# import os
#
# ios_copy_running_cfg_startup_cfg = ('''
# Destination filename [startup-config]?
# Building configuration...
# [OK]
# 0 bytes copied in 2.600 secs (0 bytes/sec)''')
#
# nx_copy_running_cfg_startup_cfg = ('''
# [########################################] 100%
# Copy complete.
# ''')
# arista_copy_running_cfg_startup_cfg = ('''
# Copy completed successfully.
# ''')
#
# clear_couters = ''' Clear "show interface" counters on all interfaces [confirm] '''
#
# def get_command_output(command, node):
#     with open(node+'.log') as file:
#         command_output = ''
#         try:
#             log = file.read()
#             if "show clock" in command:
#                 output_beg = log.index('=-=-=\n'+command)
#                 print(output_beg)
#             else:
#                 output_beg = log.index('=-=-=\n'+command+'\n'+command)
#                 output_end = log.index(node+'#', output_beg)
#                 print(output_end)
#                 command_output = log[output_beg:output_end]
#                 command_output = command_output[:command_output.rfind('\n')]
#                 command_output = command_output[command_output.find('\n')+1:]
#                 command_output = command_output[command_output.find('\n')+1:]
#                 command_output = command_output.replace('\r','')
#
#         except Exception as e:
#             print('Invalid "'+command+'" output in '+node+'.log file')
#         return command_output
#
# # commands = ["show clock", "show processes cpu history", "show call active voice compact", "show version", "show cdp neighbor detail"
# #             , "show inventory", "show environment", "show run", "show ip interface brief", "show controller t1",
# #             "show controller e1", "show isdn status", "show isdn service", "show voice port summary", "show sccp", "show ccm-manager",
# #             "show dial-peer voice summary", "show mgcp", "show gatekeeper", "show gateway", "dir", "dir all", "show ip route",
# #             "show flash", "show slot0", "copy running-config startup-config", "show memory"]
# commands = ['show clock', 'show version','show interface description','show interface status']
# for command in commands:
#
#     print(get_command_output(command, "LNUSNJSCSHW01ALR02"))
#
# node = 'LNUSNJSCSHW01ALR02'
#
# if not os.path.exists('netsim/' + node + '/' + node + '/'):
#     is_nx_device = get_command_output("show version", node).__contains__('cisco Nexus')
#     is_arista_device = get_command_output("show version", node).__contains__('Arista')
#
#
# for command in commands:
#     command_output = get_command_output(command, node)
#     if is_nx_device:
#         print(f"Nexus device:{is_nx_device}")
#         if "show running-config" in command:
#             command_output = command_output + ('\n__end_of_ned_cmd__')
#         if "show run" in command:
#             command_output = command_output + ('\n__end_of_ned_cmd__')
#         if "copy running-config startup-config" in command:
#             command_output = nx_copy_running_cfg_startup_cfg
#         if "clear counters" in command:
#             command_output = ""
#     elif is_arista_device:
#         print(f"Arista device:{is_arista_device}")
#         if "copy running-config startup-config" in command:
#             command_output = arista_copy_running_cfg_startup_cfg
#         if "clear counters" in command:
#             command_output = ""
#     else:
#         if "copy running-config startup-config" in command:
#             command_output = ios_copy_running_cfg_startup_cfg
#         if "clear counters" in command:
#             command_output = clear_couters


# retStatus = {}
# retStatus['allPassed'] = False
# print(retStatus['allPassed'])


# import difflib
# import os
# import sys
# import pandas as pd
# from bs4 import BeautifulSoup
# file1='121_pre_change_capture_USNCRTPLL0ACL0001.csv'
# file2='121_post_change_capture_USNCRTPLL0ACL0001.csv'
# file1_lines=open(file1).readlines()
# file2_lines=open(file2).readlines()
# difference=difflib.HtmlDiff().make_file(file1_lines,file2_lines,file1,file2)
#
# #difference = difflib.HtmlDiff().make_file(config, postConfig)
# data = []
# # for getting the header from the HTML file
# list_header = []
# soup = BeautifulSoup(difference, 'html.parser')
# header = soup.find_all("table")[2].find("tr")
# for items in header:
#         list_header.append(items.get_text())
# HTML_data = soup.find_all("table")[0].find_all("tr")[1:]
# for element in HTML_data:
#         sub_data = []
#         for sub_element in element:
#             try:
#                 sub_data.append(sub_element.get_text())
#             except:
#                 continue
#         data.append(sub_data)
# df = pd.DataFrame(data=data)
# df.pop(0)
# df.pop(1)
# df.pop(3)
# df.pop(4)
#     # d=list(dataframe)
#     # print(d)
# df.columns = ["     Before Commit", "       After Commit"]
# df.to_csv("Final_Result.csv")

# str = 'remedy-ms'
#
# print(str.split("-")[0])



# import openpyxl
# from pathlib import Path
# xlsx_file = Path('Testdata', 'DRAM-defective-Serial-numbers.xlsx')
#
# wb = openpyxl.load_workbook(xlsx_file)
# ws = wb.active
# serial_numbers = ws['B']
# data = []
# for x in range(len(serial_numbers)):
#     s_no = serial_numbers[x].value
#     data.append(str(s_no))
#
# #Remove duplicate entries
# unique_data = list(set(data))
# print(unique_data)
#
# with open('Testdata/s_no.txt', 'w') as f_write:
#     f_write.write(",".join(unique_data))

# commandOutputObj = [{"File": "n7000-s1-dk9.5.0.2a.bin"}, {"File": "n7000-s1-dk9.6.2.10.bin"}, {"File": "n7000-s1-kickstart.5.0.2a.bin"}, {"File": "n7000-s1-kickstart.6.2.10.bin"}]
# imageFilesList = ["n7000-s1-kickstart.6.2.10.bin", "n7000-s1-dk9.6.2.10.bin"]
# result = []
# matchFoundFlag = False
# for imageFile in imageFilesList:
#     for outputImageFile in commandOutputObj:
#         if (outputImageFile['File'] == imageFile):
#             matchFoundFlag = True
#         else:
#             matchFoundFlag = False
#         result.append(matchFoundFlag)
#
# print(result)

# list1 = [["1", "2"], ["3", "4"]]
# list3 = list(list1)
# print(list3)
# list2 = [["5", "6"], ["7", "8"]]
# for item1, item2 in zip(list3, list2):
#     print(item1, item2)

# import devpackage.DataProvider as DeviceDataProvider
# import simplejson
# import re

# dp = DeviceDataProvider.DeviceDataProvider(context)
# ctype = DeviceDataProvider.CollectionType


# Generic analysis script to process textfsm output


# def main(*args):
#     dp.job_execution_log("Executing the generic script")
#
#     result = dp.get_fields_as_dict_list(ctype.PRE, "FILE_SYSTEM", "IMAGE_NAME")
#     print("Result::::::::::::::::", result)
#     final_status = True
#     result_len = len(result)
#     reload_images_result_length = int(result_len / 2)
#     boot_file_current = result[0:result_len / 2]
#     boot_variable_set = 0
#     print("Current boot variable result:::::::", boot_file_current)
#     boot_file_next = result[result_len / 2:]
#     print("Reload boot variable result:::::::", boot_file_next)
#     reload_boot_variable_file_system = []
#     reload_boot_variable_file_name = []
#     boot_image_file_system_reload = ''
#     boot_image_name_reload = ''
#     boot_image_file_system_current = ''
#     boot_image_name_current = ''
#     allowedExt = "(bin|conf)"
#     imageFileRegExPattern = '(\S+).' + allowedExt
#
#     if result_len == 0:
#         final_status = False
#         dp.export_variable("BootImageFileSystem", boot_image_file_system_reload)
#         dp.add_pre_status_field(
#             "Boot Variable", "Not Available", "Boot Variable Check", "Fail")
#     else:
#         for i in range(0, reload_images_result_length, 2):
            # boot_image_file_system_reload = result[reload_images_result_length + i].get("FILE_SYSTEM")
            # print("Boot image file system reload:::::::::", boot_image_file_system_reload)
            # boot_image_name_reload = result[reload_images_result_length + i].get("IMAGE_NAME")
            # print("Boot image name reload:::::::::", boot_image_name_reload)
            # boot_image_file_system_current = result[i].get("FILE_SYSTEM")
            # print("Boot image file system current:::::::::", boot_image_file_system_current)
            # boot_image_name_current = result[i].get("IMAGE_NAME")
            # print("Boot image name current:::::::::", boot_image_name_current)
            # kickstart_boot_image_file_system_reload = result[reload_images_result_length + i].get("FILE_SYSTEM")
            # print("Boot image file system reload:::::::::", kickstart_boot_image_file_system_reload)
            # kickstart_boot_image_name_reload = result[reload_images_result_length + i].get("IMAGE_NAME")
            # print("Boot image name reload:::::::::", kickstart_boot_image_name_reload)
            # system_boot_image_file_system_reload = result[reload_images_result_length + i + 1].get("FILE_SYSTEM")
            # print("Boot image file system reload:::::::::", system_boot_image_file_system_reload)
            # system_boot_image_name_reload = result[reload_images_result_length + i + 1].get("IMAGE_NAME")
            # print("Boot image name reload:::::::::", system_boot_image_name_reload)
            # kickstart_boot_image_file_system_current = result[i].get("FILE_SYSTEM")
            # print("Boot image file system current:::::::::", kickstart_boot_image_file_system_current)
            # kickstart_boot_image_name_current = result[i].get("IMAGE_NAME")
            # print("Boot image name current:::::::::", kickstart_boot_image_name_current)
            # system_boot_image_file_system_current = result[i].get("FILE_SYSTEM")
            # print("Boot image file system current:::::::::", system_boot_image_file_system_current)
            # system_boot_image_name_current = result[i].get("IMAGE_NAME")
            # print("Boot image name current:::::::::", system_boot_image_name_current)
            #
            # boot_image_name_reload = list(zip(kickstart_boot_image_name_reload, system_boot_image_file_system_reload))
            # print("Combined boot image for reload:::::::", boot_image_name_reload)
            # boot_image_name_current = list(zip(kickstart_boot_image_name_current, system_boot_image_name_current))
            # print("Combined boot image for current:::::::", boot_image_name_current)

            # for kickstart_current, system_current in zip(kickstart_boot_image_name_current,
            #                                              system_boot_image_name_current):
            #     for kickstart_reload, system_reload in zip(kickstart_boot_image_name_reload,
            #                                                system_boot_image_file_system_reload):
            #         print("Values for zip data::::", kickstart_current, system_current, kickstart_reload, system_reload)
            #         if (re.search(imageFileRegExPattern, kickstart_reload) and re.search(imageFileRegExPattern,
            #                                                                              kickstart_current)
            #                 and re.search(imageFileRegExPattern, system_reload) and re.search(imageFileRegExPattern,
            #                                                                                   system_current)):
            #             final_status = True
            #             dp.add_pre_status_field("Current Boot variable matches with Reload Boot variable",
            #                                     "[" + "[" + kickstart_current + system_current + "]" + "[" + kickstart_reload + system_reload + "]" + "]",
            #                                     "OK", "Passed")
            #         else:
            #             final_status = False
            #             errMsg = 'Boot Variables are not matching'
            #             dp.add_pre_status_field("Current Boot variable matches with Reload Boot variable",
            #                                     "[" + "[" + kickstart_current + system_current + "]" + "[" + kickstart_reload + system_reload + "]" + "]",
            #                                     errMsg, 'Failed')
            #     else:
            #         final_status = False
            #         errMsg = 'Image file is not in this format ==> <file-system>:/<image-name>.bin or <file-system>:/<file-name>.conf'
            #         dp.add_pre_status_field("Current Boot variable matches with Reload Boot variable",
            #                                 "[" + "[" + kickstart_current + system_current + "]" + "[" + kickstart_reload + system_reload + "]" + "]",
            #                                 errMsg, 'Failed')
            #
            # if boot_image_file_system_reload not in reload_boot_variable_file_system:
            #     reload_boot_variable_file_system.append(boot_image_file_system_reload)
            #
            # if re.search(imageFileRegExPattern,
            #              boot_image_name_reload) and boot_image_name_reload not in reload_boot_variable_file_name:
            #     reload_boot_variable_file_name.append(boot_image_name_reload)

            # if(re.search(imageFileRegExPattern,boot_image_name_reload) and re.search(imageFileRegExPattern,boot_image_name_current)):
            #     if((boot_image_file_system_reload == boot_image_file_system_current) and (boot_image_name_reload == boot_image_name_current)):
            #         final_status = True
            #         boot_variable_set += 1
            #         dp.add_pre_status_field("Current Boot variable matches with Reload Boot variable", "["+boot_image_file_system_current +
            #                             "/"+boot_image_name_current+","+boot_image_file_system_reload+"/"+boot_image_name_reload+"]", "OK", "Passed")
            #     else:
            #         final_status = False
            #         errMsg = 'Boot Variables are not matching'
            #         dp.add_pre_status_field("Current Boot variable matches with Reload Boot variable", "["+boot_image_file_system_current +
            #                             "/"+boot_image_name_current+","+boot_image_file_system_reload+"/"+boot_image_name_reload+"]", errMsg, 'Failed')
            # else:
            #     final_status = False
            #     errMsg = 'Image file is not in this format ==> <file-system>:/<image-name>.bin or <file-system>:/<file-name>.conf'
            #     dp.add_pre_status_field("Current Boot variable matches with Reload Boot variable", "["+boot_image_file_system_current +
            #                             "/"+boot_image_name_current+","+boot_image_file_system_reload+"/"+boot_image_name_reload+"]", errMsg, 'Failed')

            # if boot_image_file_system_reload not in reload_boot_variable_file_system:
            #     reload_boot_variable_file_system.append(boot_image_file_system_reload)

            # if re.search(imageFileRegExPattern,boot_image_name_reload) and boot_image_name_reload not in reload_boot_variable_file_name:
            #     reload_boot_variable_file_name.append(boot_image_name_reload)

    # print("Boot image file name::::::::", reload_boot_variable_file_name)
    # dp.export_variable("BootImageFileSystem", simplejson.dumps(reload_boot_variable_file_system))
    # dp.export_variable("BootImageName", simplejson.dumps(reload_boot_variable_file_name))
    #
    # if boot_variable_set >= 2:
    #     dp.publish_pre_status(True, "Pre check passed")
    # else:
    #     dp.publish_pre_status(False, "Pre check failed")
    #
    # json = dp.publish_status()
    # return json


# models = '''
# DCS-7150S-24-R,
# DCS-7124SX-F,
# DCS-7150S-24-F,
# DCS-7280SR-48C6-F,
# DCS-7150S-52-CL-R,
# DCS-7150S-64-CL-F,
# DCS-7150S-52-CL-F,
# DCS-7150S-64-CL-R,
# DCS-7150S-64-CL-SSD-F,
# DCS-7150S-24-CL-F,
# DCS-7020TR-48-F,
# DCS-7280SE-64-R,
# DCS-7010T-48,
# DCS-7010T-48-R,
# DCS-7050QX-32S-F,
# DCS-7280SE-64-F,
# DCS-7280SR2-48YC6-F,
# DCS-7508,
# DCS-7050SX-128-F,
# DCS-7148SX-F,
# DCS-7280SR-48C6-R,
# DCS-7150S-64-CL-SSD-R,
# DCS-7020TR-48-R,
# DCS-7060CX-32S-F,
# DCS-7508N,
# DCS-7050SX3-96YC8,
# DCS-7060CX2-32S-F,
# DCS-7280QR-C36-F,
# DCS-7060SX2-48YC6-R,
# DCS-7280SR2-48YC6-R,
# DCS-7050SX-72Q-F,
# DCS-7280CR2-60-F,
# DCS-7050SX2-128-F,
# DCS-7050SX-72Q-R,
# DCS-7504N,
# DCS-7504
# '''
#
# data = list(value.replace("\n","") for value in models.split(","))
# data.sort()
#
# print(",".join(data))

# import json
# file_path= "/Users/vibodapa/Documents/BPA-3.2.2/AS-BAC-BPA/microservices/bpa-service-pack/data/BranchModifySwitchConfigurationV1P4P0/process-templates/Templates.json"
#
# with open("Testdata/Templates.json", "r") as f_read:
#     data = f_read.readlines()
#     print(data)

vlan_id = 12
vlan_list = [1, 2]
print(f"Vlan ID {str(vlan_id)}, Vlans allowed on trunk {','.join(map(str, vlan_list))}")
print(",".join(map(str, vlan_list)))
