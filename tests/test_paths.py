from project.helpers import ROOT_DIR
#from project.helpers import PROJECT_DATA_DIR
import os
import pytest

if not os.environ.get("PROJECT_DATA_DIR"):
    pytest.skip(
        "PROJECT_DATA_DIR не задан: проверки путей пропущены",
        allow_module_level=True,
    )

def test_root_dir_exists():
    assert ROOT_DIR.exists()

def test_root_dir_is_dir():
    assert ROOT_DIR.is_dir()


""" Необходимо раскомментировать тесты ниже (и import в начале файла), если для хранения data используется .env """
# def test_project_data_dir_exists():
#     assert PROJECT_DATA_DIR.exists()

# def test_project_data_dir_is_dir():
#     assert PROJECT_DATA_DIR.is_dir()
