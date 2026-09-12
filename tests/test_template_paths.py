from project.helpers import PROJECT_DATA_DIR, ROOT_DIR


def test_root_dir_exists():
    assert ROOT_DIR.exists()

def test_root_dir_is_dir():
    assert ROOT_DIR.is_dir()

def test_project_data_dir_exists():
    assert PROJECT_DATA_DIR.exists()

def test_project_data_dir_is_dir():
    assert PROJECT_DATA_DIR.is_dir()
