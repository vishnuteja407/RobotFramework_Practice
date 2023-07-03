# def add_fun(*args):
#     sum = 0
#     for number in args:
#         sum+=number
#
#     return sum
#
# print(add_fun(2,3,4,5,6,7,8,9,10))


# def data_processing(**kwargs):
#     print(kwargs.items())
#     for key, value in kwargs.items():
#         print("{} is {}".format(key, value))
#         print(f"{key} is {value}")
#
# data_processing(name="abcd", age=22, occupation="job", location="Bangalore")

# def square(x):
#     a,b = x
#     return a*b
#
# list1 = [(1,2),(3,4),(5,6)]
#
# list2 = list(map(lambda x:x[0]*x[1], list1))
# print(list2)


# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = list(filter(lambda x: x%2==0, list1))
# print(list2)


# from functools import reduce
#
# addition = reduce(lambda x,y: x+y, list1)
# print(addition)
#
# print(sum(list1))

# count = 0
# n=99
# for i in range(0, n):
#     print(i)
#     for j in range(0, n):
#         count = count+1
# for k in range(0, n):
#     count = count - 1
#
# print(count)

# arr = [[1, 2, 3, 4, 5],
#        [4, 6, 7, 8, 9],
#        [1, 2, 4, 5, 6],
#        [1, 2, 4, 5, 6],
#        [5, 6, 8, 9, 1]]
# print(arr[1][4])
# print(arr)
# n = 5
# principal = []
# for k in range(1, n+1):
#     result = 0
#     for i in range(0, k):
#         for j in range(0, n):
#             if ((i + j) == (n - 1)):
#                 result += arr[n-i-1][n-j-1]
#     principal.append(result)
#
# print(principal)
import logging
# result = {
#     "status": "success",
#     "data": {
#         "resultType": "vector",
#         "result": [
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb-arb:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.217:27017",
#                     "set": "bpa",
#                     "state": "ARBITER"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb-arb:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.95:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb-arb:6081",
#                     "job": "mongodb",
#                     "name": "30.133.174.126:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb-arb:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.200:27017",
#                     "set": "bpa",
#                     "state": "PRIMARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb-arb:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.201:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb1:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.217:27017",
#                     "set": "bpa",
#                     "state": "ARBITER"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb1:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.95:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb1:6081",
#                     "job": "mongodb",
#                     "name": "30.133.174.126:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb1:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.200:27017",
#                     "set": "bpa",
#                     "state": "PRIMARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb1:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.201:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb2:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.217:27017",
#                     "set": "bpa",
#                     "state": "ARBITER"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb2:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.95:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb2:6081",
#                     "job": "mongodb",
#                     "name": "30.133.174.126:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb2:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.200:27017",
#                     "set": "bpa",
#                     "state": "PRIMARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb2:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.201:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb4:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.217:27017",
#                     "set": "bpa",
#                     "state": "ARBITER"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb4:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.95:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb4:6081",
#                     "job": "mongodb",
#                     "name": "30.133.174.126:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb4:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.200:27017",
#                     "set": "bpa",
#                     "state": "PRIMARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb4:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.201:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb5:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.217:27017",
#                     "set": "bpa",
#                     "state": "ARBITER"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb5:6081",
#                     "job": "mongodb",
#                     "name": "30.133.127.95:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb5:6081",
#                     "job": "mongodb",
#                     "name": "30.133.174.126:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb5:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.200:27017",
#                     "set": "bpa",
#                     "state": "PRIMARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "mongodb_mongod_replset_member_health",
#                     "instance": "mongodb5:6081",
#                     "job": "mongodb",
#                     "name": "30.140.200.201:27017",
#                     "set": "bpa",
#                     "state": "SECONDARY"
#                 },
#                 "value": [
#                     1654156308.994,
#                     "1"
#                 ]
#             }
#         ]
#     }
# }
result = {
    "status": "success",
    "data": {
        "resultType": "vector",
        "result": [
            {
                "metric": {
                    "__name__": "pg_up",
                    "instance": "postgresdb1:6082",
                    "job": "postgresql"
                },
                "value": [
                    1655103964.442,
                    "0"
                ]
            },
            {
                "metric": {
                    "__name__": "pg_up",
                    "instance": "postgresdb2:6082",
                    "job": "postgresql"
                },
                "value": [
                    1655103964.442,
                    "1"
                ]
            },
            {
                "metric": {
                    "__name__": "pg_up",
                    "instance": "postgresdb3:6082",
                    "job": "postgresql"
                },
                "value": [
                    1655103964.442,
                    "1"
                ]
            }
        ]
    }
}
# print(type(result))
def postgres_status(result):
    """Checks three Postgres DB Status
    :param result: response received by probing postgres database
    :return: postgres database status
    """
    failedDataList = []
    successDataList = []
    retStatus = {}
    failed_count = 0
    for metric_data in result['data']['result']:
        # print(metric_data)
        instance = metric_data.get('metric').get('instance')
        value = metric_data.get('value')
        if int(value[1]) == 1:
            status_up = metric_data
            successDataList.append({'instance': instance, 'statusCode': value[1], 'message': '{} is up'.format(instance)})
        else:
            failed_count = failed_count + 1
            failedDataList.append({'instance': instance, 'statusCode': value[1], 'message': '{} is down'.format(instance)})
    if failed_count == 0:
        retStatus['allPassed'] = True
        retStatus['failedDataList'] = []
        retStatus['successDataList'] = successDataList
        logging.info('Return postgres_status :: {}'.format(retStatus))
        return retStatus
    else:
        retStatus['allPassed'] = False
        retStatus['failedDataList'] = failedDataList
        retStatus['successDataList'] = successDataList
        logging.info('Return postgres_status :: {}'.format(retStatus))
        return retStatus


print(postgres_status(result))