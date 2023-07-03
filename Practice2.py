import logging
import simplejson

MICROSERVICES = ['camunda', 'camunda-external-tasks', 'kong', 'auth-service', 'bac-services-ms', 'cmd-analyzer', 'core-services', 'cwm-ms',
                 'market-variance', 'milestones-ms', 'portal', 'service-catalog-ms','remedy',
                 'nidm-system-ms', 'ncd-ms','eps-ms', 'hsm-init-ms','cms-p']
MICROSERVICES.sort()
print(MICROSERVICES)
#['auth-service', 'bac-services-ms', 'camunda', 'camunda-external-tasks', 'cmd-analyzer', 'cms-p', 'core-services', 'cwm-ms',
# 'eps-ms', 'hsm-init-ms', 'kong', 'market-variance', 'milestones-ms', 'ncd-ms', 'nidm-system-ms', 'portal', 'remedy', 'service-catalog-ms']

# result = {
#     "status": "success",
#     "data": {
#         "resultType": "vector",
#         "result": [
#             {
#                 "metric": {
#                     "__name__": "probe_success",
#                     "instance": "http://camunda:8080/engine-rest/engine",
#                     "job": "services"
#                 },
#                 "value": [
#                     1655138229.978,
#                     "200"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "probe_success",
#                     "instance": "http://kong:8001",
#                     "job": "services"
#                 },
#                 "value": [
#                     1655138229.978,
#                     "200"
#                 ]
#             },
#             {
#                 "metric": {
#                     "__name__": "probe_success",
#                     "instance": "https://camunda-external-tasks:9222/about/cisco-bpa-platform/mw-camunda-external-tasks",
#                     "job": "services"
#                 },
#                 "value": [
#                     1655138229.978,
#                     "500"
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
                    "__name__": "probe_http_status_code",
                    "instance": "http://camunda:8080/engine-rest/engine",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "http://kong:8001",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://auth-service:9202/about/cisco-bpa-platform/mw-auth",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://auth-service:9202/api/v1.0/monitor/db-health-check",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://bac-services-ms:9216/about/cisco-bpa-robot-platform/mw-bac-services-ms",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://camunda-external-tasks:9222/about/cisco-bpa-platform/mw-camunda-external-tasks",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://cmd-analyzer:9876",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://cms-p:9219/about/cisco-bpa-robot-platform/mw-cms-p",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/about/cisco-bpa-platform/mw-core",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/db-health-check/cisco-bpa-platform/mw-core",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_56",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_56/nso5-lsa0-r2",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_56/nso5-lsa3-rb",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_56/nso5-lsa3-rd",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_56/nso5-lsa3-re",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_56/nso5-lsa5-r1",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "401"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_61",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_61/nso5-lsa4-rb",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_61/nso5-lsa4-rd",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_61/nso5-lsa4-re",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1.0/nso/nsoConnection?nsoHostname=RTP_NSO_61/nso5-rnetsim4",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://core-services:9201/api/v1/mail/healthcheck",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://cwm-ms:9212/about/cisco-bpa-robot-platform/mw-cwm-ms",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://cwm-ms:9212/api/v1.0/db-health-check/cisco-bpa-robot-platform/mw-cwm-ms",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://cwm-ms:9212/api/v1.0/monitor/health-check",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "500"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://cwm-ms:9212/api/v1.0/monitor/rabbitmq-connection-check",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "500"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://eps-ms:9217/about/cisco-bpa-robot-platform/mw-eps",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://eps-ms:9217/api/v1.0/db-health-check/cisco-bpa-robot-platform/mw-eps",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://hsm-init-ms:9215/about/cisco-bpa-robot-platform/mw-hsm-init-ms",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://market-variance:9205/about/cisco-bpa-platform/mw-market-variance",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://market-variance:9205/api/v1.0/db-health-check/cisco-bpa-platform/mw-market-variance",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://milestones-ms:9211/about/cisco-bpa-platform/mw-milestones",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://milestones-ms:9211/api/v1.0/db-health-check/cisco-bpa-platform/mw-milestones",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://ncd-ms:9221/about/cisco-bpa-robot-platform/mw-ncd",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://ncd-ms:9221/api/v1.0/db-health-check/cisco-bpa-robot-platform/mw-ncd",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://nidm-system-ms:9214/about/cisco-bpa-robot-platform/mw-nidm-system-ms",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://nidm-system-ms:9214/nidm/api/v1/monitor/health-check",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://portal:8081",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://remedy:9218/about/cisco-bpa-robot-platform/mw-remedy",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://remedy:9218/api/v1.0/db-health-check/cisco-bpa-robot-platform/mw-remedy",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://remedy:9218/api/v1.0/monitor/health-check",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://service-catalog-ms:9210/about/cisco-bpa-platform/mw-service-catalog",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            },
            {
                "metric": {
                    "__name__": "probe_http_status_code",
                    "instance": "https://service-catalog-ms:9210/api/v1.0/db-health-check/cisco-bpa-platform/mw-service-catalog",
                    "job": "services"
                },
                "value": [
                    1655186040.803,
                    "200"
                ]
            }
        ]
    }
}
def get_message(uri_data, instance, microservice, service_mode):
    if 'about' in uri_data:
        message = 'Service is {}'.format(service_mode)
    elif 'db-health-check' in uri_data:
        message = 'Service is{notStr} able to connect to DB'.format(notStr=' not' if service_mode == 'down' else '')
    elif 'health-check' in uri_data:
        message = 'BPA is{notStr} able to connect to {} external application'.format(microservice, notStr=' not' if service_mode == 'down' else '')
    elif 'rabbitmq-connection-check' in uri_data:
        message = 'BPA is{notStr} able to connect to Rabbit MQ'.format(microservice,
                                                                       notStr=' NOT' if service_mode == 'down' else '')
    elif 'mail' in uri_data:
        message = 'BPA is{notStr} able to connect to SMTP'.format(notStr=' not' if service_mode == 'down' else '')
    elif instance.find('nsoConnection') != -1:
        nsoName = instance.split('=')[-1]
        message = 'BPA is{notStr} able to connect to NSO {}'.format(nsoName, notStr=' not' if service_mode == 'down' else '')
    else:
        message = 'Service is {}'.format(service_mode)
    return message


def ms_status(result):
    """Checks microservice status that are critical for BPA

    :param result: json response received by probing BPA microservices that are critical
    :return: critical BPA microservice up status
    """
    failedDataList = []
    successDataList = []
    retStatus = {}
    allPassed = True
    for metric_data in result["data"]["result"]:
        # print(metric_data)
        instance = metric_data.get("metric").get("instance")
        value = metric_data.get("value")

        for microservice in MICROSERVICES:
            if instance.split("//")[1].split(":")[0] == microservice:
                if int(value[1]) != 200:
                    allPassed = False
                    splitter = instance.split('/')
                    message = get_message(splitter, instance, microservice, 'down')
                    failedDataList.append({'statusCode': value[1], 'microservice': microservice, 'message': message})
                else:
                    splitter = instance.split('/')
                    message = get_message(splitter, instance, microservice, 'up')
                    successDataList.append({'statusCode': value[1], 'microservice': microservice, 'message': message})

    retStatus['allPassed'] = allPassed
    retStatus['failedDataList'] = failedDataList
    retStatus['successDataList'] = successDataList
    logging.info('Return ms_status :: {}'.format(retStatus))
    return retStatus

response = ms_status(result)
json_object = simplejson.dumps(response, indent=4)
with open("Testdata/api_response.json", "w") as f:
    f.write(json_object)


