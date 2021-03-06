from configparser import ConfigParser
from typing import Dict
from pathlib import Path

# filepath to .ini file for auth credentials
p = Path('.') / 'settings/grocer.ini'
config_path = p.absolute()
 
def config_dict(filename: Path = config_path, section: str = 'DATABASE') -> Dict:
    """
    read ini file and return section dict. 
    """
    # create a parser and read file
    parser = ConfigParser()
    parser.read(filename)

    # Checks to see if section (postgresql) parser exists
    if not parser.has_section(section):
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    params = parser.items(section)
    return {param[0]: param[1] for param in params}

if __name__ == '__main__':
    print(p)
    print(config_dict())