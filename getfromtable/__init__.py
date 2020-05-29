import logging
import requests
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    # try:
    #     req_body = req.get_json()
    # except ValueError:
    #     pass
    # else:
    #     url = req_body["url"]

    #     if url:
    #         headers = {"Accept": "application/json;odata=nometadata"}
    #         data = x.json()
    #         dataJson = json.dumps(data)
    #         return func.HttpResponse(
    #                 body=dataJson, status_code=200, mimetype= "application/json")
    #     else:
    #         return func.HttpResponse(
    #             "Please send the URL",
    #             status_code=400
    #         )

    headers = {"Accept": "application/json;odata=nometadata"}
    x = requests.get("https://storageraumueberwachung.table.core.windows.net/Last2()?sv=2019-10-10&ss=bfqt&srt=sco&sp=rwdlacupx&se=2023-07-31T22:47:36Z&st=2020-05-13T14:47:36Z&spr=https&sig=4skbsTU9tMlfSqFJhB1rTw16nVRIA6EVzxEkCmrNneE%3D", headers=headers)
    data = x.json()
    dataJson = json.dumps(data)

    return func.HttpResponse(
        body=dataJson, status_code=200, mimetype= "application/json")


# "https://storageraumueberwachung.table.core.windows.net/Raw2()?sv=2019-10-10&ss=bfqt&srt=sco&sp=rwdlacupx&se=2023-07-31T22:47:36Z&st=2020-05-13T14:47:36Z&spr=https&sig=4skbsTU9tMlfSqFJhB1rTw16nVRIA6EVzxEkCmrNneE%3D&$filter=PartitionKey%20eq%20'device01_al_illuminance'"

# requestTimestamp = ""

# allSensorsLatestData = "&$filter=Device_Id%20eq%20'device01'%20and%20Sensor_Id%20eq%20'aq_temperature'%20and%20Timestamp%20gt%20datetime" + "'" + requestTimestamp + "'"

# &$filter=PartitionKey%20eq%20'device01_al_illuminance'
# &$filter=Device_Id%20eq%20'device01'%20and%20Sensor_Id%20eq%20'aq_temperature'%20and%20Timestamp%20gt%20datetime'2020-05-13T19:35:02.2401372Z'