from dotenv import load_dotenv
from omegaconf.resolvers import oc

from .helpers import ROOT_DIR
from .hooks import ExperimentMetadataHook

load_dotenv(ROOT_DIR / ".env")

HOOKS = (ExperimentMetadataHook(),)

CONFIG_LOADER_ARGS = {
    "base_env": "base",
    "default_run_env": "local",
    "custom_resolvers": {
        "oc.env": oc.env
    }
}
