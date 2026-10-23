from dotenv import load_dotenv
from omegaconf.resolvers import oc

from .helpers import ROOT_DIR

load_dotenv(ROOT_DIR / ".env")

CONFIG_LOADER_ARGS = {
    "custom_resolvers": {
        "oc.env": oc.env
    }
}
