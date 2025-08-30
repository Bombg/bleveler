import tls_client
import json
from Settings import Settings
import time
import logging
from datetime import datetime
from zoneinfo import ZoneInfo
import colorlog

baseSettings = Settings()

logger = logging.getLogger(__name__)
logger.setLevel(baseSettings.LOG_LEVEL)
handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(bold)s%(levelname)s:%(name)s:%(message)s")
)
handlers = [handler]
logging.basicConfig(level=baseSettings.LOG_LEVEL, handlers=handlers)

tzInfo = ZoneInfo(baseSettings.TZ)
fightsDone = {}

def SendChatMessage(content):
    url = "https://kick.com/api/v1/chat-messages"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": baseSettings.USER_AGENT,
        "Authorization": f"Bearer {baseSettings.AUTHORIZATION}",
    }
    # r.headers["X-Xsrf-Token"] = ""
    r = tls_client.Session(client_identifier="firefox_120", random_tls_extension_order=True)
    r.headers = headers 
    message = {"message": content, "chatroom_id": baseSettings.CHATROOM_ID}
    messageJson = json.dumps(message)
    response = r.post(url, headers=headers, json=messageJson)
    if response.status_code != 200:
        logger.warning(f"StatusCode:{response.status_code}")

def StartFights():
    for rival in baseSettings.RIVALS:
        content = f"!bduel {rival}"
        logger.info(f"Fighting: {rival}")
        SendChatMessage(content)
        time.sleep(baseSettings.SECONDS_BETWEEN_BATTLES)
        content = "!blevelup"
        SendChatMessage(content)
        time.sleep(baseSettings.SECONDS_AFTER_BATTLE)

if __name__ == "__main__":
    nowTime = datetime.now(tzInfo)
    dateString = nowTime.strftime("%d/%m/%Y")
    hour = nowTime.hour
    logger.info("bleveler started")
    logger.info(f"Fights start at: {baseSettings.FIGHT_TIME} it's now {hour}")
    while True:
        nowTime = datetime.now(tzInfo)
        dateString = nowTime.strftime("%d/%m/%Y")
        if nowTime.hour != hour:
            hour = nowTime.hour
            logger.info(f"Fights start at: {baseSettings.FIGHT_TIME} it's now {hour}")
        if dateString not in fightsDone and hour == baseSettings.FIGHT_TIME:
            fightsDone[dateString] = 1
            StartFights()
        time.sleep(baseSettings.SECONDS_BETWEEN_FIGHT_CHECK)