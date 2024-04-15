from configparser import ConfigParser as CF


def get_token(section: str) -> str:
    config = CF()
    config.read("config.ini")
    return config[section]["TG_Bot"]
