
from icecream import ic, install

from config.settings import ENVIRONMENT

if ENVIRONMENT == "TEST":
    install()
    ic.configureOutput(prefix="ic-debug| ", includeContext=True)
    ic("ic configured")

