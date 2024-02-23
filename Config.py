import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21119132"))
    API_HASH = os.environ.get("API_HASH", "c0a90d0ba66e6bdea356894a55f4856e)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6704245576:AAGqYQrMMuH2yt2sHJ9Zhk7q2wtNrDA_Eow")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBu004Bhr3WvlbDwYdzJfdMzjrgXDo5nh_AqXybILcvL4PECn3WosR1TcyOkMDssz9MmMcaEf4Y44nLgqsgfVvjQRoUWqxneu8EJ8A4NcbpfoxBSkdf9wWcH8WHdx0VHExf1F1o85eZMrDqucPZcOiOh3u-bXtXZVSvzWSPKXsqT3yJPlI8lJ7wWbBUbUOW6uaIh8HiFxqdKObaFRaNLJLbOyZWnWrPhbCxMCNgOzIrK4mIdUPD_RNFWl_ibORSyoUfBB1koW7zPXfsEAxXzGCaoSekT64zrkzzXQgVUgfzx-KRk8R5qJa0JL71AFhpBm-bvJaW0faRMz6zWahAPCrh18=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "vefamusicbot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5905988205")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
