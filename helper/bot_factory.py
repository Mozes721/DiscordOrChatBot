from bot.local_bot import LocalBot
from bot.discord_bot import DiscordBot

class BotFactory:
    @staticmethod
    def create_bot(deployment, service):
        if deployment:
            return DiscordBot(service)
        else:
            return LocalBot()