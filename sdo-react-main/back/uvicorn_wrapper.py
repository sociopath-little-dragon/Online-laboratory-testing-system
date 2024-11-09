import uvicorn
import os
from modules.configs.config_funcs import load_config

config = load_config()

# os.environ["DB_CON"] = "sqlite:///database/tst.db?check_same_thread=False"
os.environ["DB_CON"] = "sqlite:///sdo-react-main/back/database/tst.db?check_same_thread=False"
# os.environ["DB_CON"] = "sqlite:///tst.db?check_same_thread=False"
from main import app
uvicorn.run(app, host=config["uvicorn"]["host"], port=config["uvicorn"]["port"])
