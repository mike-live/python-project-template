from project.helpers import ROOT_DIR


def test_root_dir_exists():
    assert ROOT_DIR.exists()

def test_root_dir_is_dir():
    assert ROOT_DIR.is_dir()

