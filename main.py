import os
import subprocess
from helper.bot_factory import BotFactory
from helper.bot_service import BotService
from api.requests import APIRequests
from config.config_files import APIkeys

def main():
    DEPLOYMENT = APIkeys.deployment  # Get deployment flag from configuration

    if not DEPLOYMENT:
        # If not deployed, launch LocalBot via Streamlit
        local_bot_path = os.path.join(os.path.dirname(__file__), "bot", "local_bot.py")
        subprocess.run(["streamlit", "run", local_bot_path], check=True)
    else:
        # If deployed, launch DiscordBot or any other bot
        api_requests = APIRequests()
        bot_service = BotService(api_requests)
        bot = BotFactory.create_bot(DEPLOYMENT, bot_service)

        if bot:
            bot.run()

if __name__ == "__main__":
    main()