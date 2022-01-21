import yaml
import settings
from pkgutil import get_data

f = get_data("settings", "logging.yaml")
a = yaml.safe_load(f)
print(a)


# from opennem.core.loader import load_data





# def load_logging_config(filename: str = "logging.yml", fail_silent: bool = True) -> Optional[dict]:
#     """ Load logging configuration from yml file """

#     settings_file_content = load_data(filename, from_settings=True)

#     if not settings_file_content:
#         if fail_silent:
#             return None

#         raise SettingsNotFound("Not a valid logging settings file: {}".format(filename))

#     config_data = yaml.safe_load(settings_file_content)

#     return config_data


# LOGGING_CONFIG = load_logging_config()