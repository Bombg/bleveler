from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import  StrictStr


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    X_CLIENT_TOKEN: str = "e1393935a959b4020a4491574f6490129f678acdaa92760471263db43487f823"
    X_XSRF_TOKEN:str = ""
    COOKIES:StrictStr = ""
    USER_AGENT:str = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    AUTHORIZATION: str = ""
    CLIENT_IDENTIFIER: str = "firefox_120"
    CHATROOM_ID: int = 0
    RIVALS: list[str] = [
        "FlexieFae",
        "Bay420",
        "lorddeathdx",
        "dogsrule",
        "Dash_D",
        "joebchill",
        "sophie017",
        "Skyler_4200",
        "Swuave",
        "Gobzz",
        "Mista_Jay24",
        "nicholastoras01",
        "UriLoufi",
        "StoneySyrup",
        "Nikione0one",
    ]
    SECONDS_BETWEEN_BATTLES: int = 90
    SECONDS_AFTER_BATTLE:int = 5
    SECONDS_BETWEEN_FIGHT_CHECK:int = 60
    LOG_LEVEL:int = 20
    TZ:str = "America/Chicago"
    FIGHT_TIME:int = 10