import os
import sys
from pathlib import Path
from typing import Any, List, Optional
from pkgutil import get_data, get_loader

MODULE_PATH = Path(os.path.dirname(sys.modules["grocer"].__file__))
PROJECT_ROOT = MODULE_PATH.parent
# @TODO add core/data location for default.
DATA_PATH = "test/fixtures"
FIXTURE_PATH = "test/fixtures"
SETTINGS_PATH = "settings"
PROJECT_DATA_PATH = "data"

def load_data(
    file_name: str,
    from_project: bool = False,
    from_fixture: bool = False,
    from_settings: bool = False,
    skip_loaders: bool = False,
    return_path: bool = False,
    content_type: str = "utf-8",
) -> Any:
    """
    Load a CSV or JSON data file from either the library
    or project data directory

    default loads from `test/fixtures`

    from_project is `test/fixtures`

    from_fixture is `test/fixtures`

    """
    data_path = (
        PROJECT_DATA_PATH
        if from_project
        else FIXTURE_PATH
        if from_fixture
        else SETTINGS_PATH
        if from_settings
        else DATA_PATH
    )

    file_path = Path(file_name)

    if return_path:
        module_path = Path(get_loader("grocer").path).parent
        return module_path / data_path / file_name

    data_content = get_data("grocer", os.path.join(data_path, file_name))

    if not data_content:
        return None

    if skip_loaders:
        return data_content.decode(content_type)

    return data_content

print(Path(get_loader("settings").path).parent)