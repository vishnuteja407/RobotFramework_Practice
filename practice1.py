import logging
import simplejson

def reading_data(file_path):
    with open(file_path) as f_read:
        data = simplejson.load(f_read)
        return data

result = reading_data("Testdata/Mongo-PHM-A1SUp.json")


def mongo_status(result):
    """Checks MongoDB Status Primary or Secondary along with Arbiter DB Node
    :param result: json response received by probing Mongo database
    :return: Mongo database status
    """
    failedDataList = []
    successDataList = []
    retStatus = {}
    db_status_primary = False
    db_status_secondary = False
    db_status_arbiter = False
    for metric_data in result['data']['result']:
        instance = metric_data.get("metric").get("instance")
        name = metric_data.get("metric").get("name")
        state = metric_data.get("metric").get("state")
        value = metric_data.get("value")
        # print(state)
        if state == 'PRIMARY':
            if int(value[1]) == 1:
                db_status_primary = True
                successDataList.append({'instance': instance, 'statusCode': value[1], 'databaseName': name, 'message': 'PRIMARY DB : {} is up'.format(name)})
            # else:
            #     db_status_primary = False
            #     failedDataList.append({'instance': instance, 'statusCode': value[1], 'databaseName': name, 'message': 'PRIMARY DB : {} is down'.format(name)})

        elif state == 'SECONDARY':
            if int(value[1]) == 1:
                db_status_secondary = True
                successDataList.append({'instance': instance, 'statusCode': value[1], 'databaseName': name, 'message': 'SECONDARY DB : {} is up'.format(name)})
            # else:
            #     db_status_secondary = False
            #     failedDataList.append({'instance': instance, 'statusCode': value[1], 'databaseName': name, 'message': 'SECONDARY DB : {} is down'.format(name)})
        elif state == 'ARBITER':
            if int(value[1]) == 1:
                db_status_arbiter = True
                successDataList.append({'instance': instance, 'statusCode': value[1], 'databaseName': name, 'message': 'ARBITER DB : {} is up'.format(name)})
            # else:
            #     db_status_arbiter = False
            #     failedDataList.append({'instance': instance, 'statusCode': value[1], 'databaseName': name, 'message': 'ARBITER DB : {} is down'.format(name)})
        else:
            failedDataList.append({'instance': instance, 'statusCode': value[1], 'databaseName': name, 'message': 'DB State is : {}'.format(state)})

    if (db_status_arbiter and db_status_primary) or (db_status_secondary and db_status_primary):
        retStatus['allPassed'] = True
        retStatus['failedDataList'] = failedDataList
        retStatus['successDataList'] = successDataList
        logging.info('Return mongo_status :: {}'.format(retStatus))
        return retStatus
    else:
        retStatus['allPassed'] = False
        retStatus['failedDataList'] = failedDataList
        retStatus['successDataList'] = successDataList
        logging.info('Return mongo_status :: {}'.format(retStatus))
        return retStatus


print(mongo_status(result))