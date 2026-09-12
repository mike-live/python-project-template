import pathlib
from project.helpers.root_dir import ROOT_DIR
from environs import Env

env = Env()
env.read_env()

PROJECT_DATA_DIR = env.path("PROJECT_DATA_DIR")

if not PROJECT_DATA_DIR.exists():
    raise ValueError(f"Project data directory does not exist: {PROJECT_DATA_DIR}")
if not PROJECT_DATA_DIR.is_dir():
    raise ValueError(f"Project data directory is not a directory: {PROJECT_DATA_DIR}")
if not PROJECT_DATA_DIR.is_absolute():
    raise ValueError(f"Project data directory is not an absolute path: {PROJECT_DATA_DIR}")