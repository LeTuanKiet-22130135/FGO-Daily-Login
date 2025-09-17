import os
import requests
import time
import json
import fgourl
import user
import coloredlogs
import logging

# Enviroments Variables
userIds = ""
authKeys = ""
secretKeys = ""
fate_region = ""
webhook_discord_url = ""
UA = ""

if UA != 'nullvalue':
    fgourl.user_agent_ = "Dalvik/2.1.0 (Linux; U; Android 13; SM-G780G Build/TP1A.220624.014)"

userNums = len(userIds)
authKeyNums = len(authKeys)
secretKeyNums = len(secretKeys)

logger = logging.getLogger("FGO Daily Login")
coloredlogs.install(fmt='%(asctime)s %(name)s %(levelname)s %(message)s')


def get_latest_verCode():
    endpoint = ""

    if fate_region == "NA":
        endpoint += "https://raw.githubusercontent.com/O-Isaac/FGO-VerCode-extractor/refs/heads/next/na.json"
    else:
        endpoint += "https://raw.githubusercontent.com/O-Isaac/FGO-VerCode-extractor/refs/heads/next/jp.json"

    response = requests.get(endpoint).text
    response_data = json.loads(response)

    return response_data['verCode']


def main():
        logger.info('Getting Lastest Assets Info')
        fgourl.set_latest_assets()

        try:
            instance = user.user(userIds, authKeys, secretKeys) 
            time.sleep(3)
            logger.info('Loggin into account!')
            instance.topLogin()
            logger.info('Loggin success')
            time.sleep(2)
            instance.topHome()
            time.sleep(2)
            logger.info('Throw daily friend summon!')
            instance.drawFP()
            time.sleep(2)
        except Exception as ex:
            logger.error(ex)


if __name__ == "__main__":
    main()
