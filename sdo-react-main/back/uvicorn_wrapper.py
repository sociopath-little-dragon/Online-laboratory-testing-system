import uvicorn
import os
from modules.configs.config_funcs import load_config

config = load_config()

os.environ["DB_CON"] = "sqlite:///database/tst.db"
from main import app
uvicorn.run(app, host=config["uvicorn"]["host"], port=config["uvicorn"]["port"])
