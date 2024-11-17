# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25729343"))
API_HASH = getenv("API_HASH", "91be96eb4ab6c52e9834cf485e7e25db")
BOT_TOKEN = getenv("BOT_TOKEN", "7785161312:AAEtjqobr-VZlYViNfYWpMKboiLMk8PgAPo")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7336971189").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://sujay283873:sujay283873@cluster028736373.dwtvw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster028736373")
LOG_GROUP = getenv("LOG_GROUP", "-1002365739972")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002434812351"))
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002362598997"))
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "BQGImT8AkIrLqDI83MQ1oZuMQMpP008XCoEsOvr_Elo_O3TuYL58x6dWK8a9r7E0gLBYjN2c9o3fDTNqsEjfvJgzylGpWNAgidaO9jQKsJGeyairEZ52OehYborP7iKs6Iw0J2HPKEqcMvwcaXBPebK1QFOOhlS7x28Qg3LrcBSMze11gEFMmXb4n-MLDG6hGIwx1nL-ysRqoMeFZJ8xT-mI9bAGNJa6lkUNlvg50N9GHjOp2bSg6yxukCQe94gvEyE5J6quEG9q92-G23YT0TNI0dqGuFjyXnPgRWq9VM0_6C-krNvqWEe3s1oK3f6sgDE7zcI7Va4Yl5zRvVeE0RwBu_fCFQAAAAFcTlThAA")
