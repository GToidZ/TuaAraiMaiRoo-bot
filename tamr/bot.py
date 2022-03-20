import logging
import hikari
import tanjun
from . import Configuration

class TamrBot:
    
    def __init__(self, config_path: str="config.json"):
        self.__config = Configuration(config_path)
        self.make_bot()

    @property
    def config(self):
        return self.__config

    def make_bot(self):
        token_query = self.config.query_key_by_keywords("token", "bot_token")
        try:
            success = False
            for _, tok in token_query:
                try:
                    bot = hikari.GatewayBot(tok)
                    try:
                        self.register_handlers(bot)
                        self.make_tanjun(bot)
                    except RuntimeError:
                        pass
                    bot.run()
                    success = True
                    break
                except hikari.UnauthorizedError:
                    pass
            if not success:
                logging.error("No tokens in configuration can be used to login")
        except:
            logging.error("No bot token set! " +
                "Please set in configuration file with option 'token'")
            exit(1)

    def register_handlers(self, bot: hikari.GatewayBot):
        pass

    def make_tanjun(self, bot: hikari.GatewayBot):
        client = (
            tanjun.Client.from_gateway_bot(
                bot,
                mention_prefix=True,
                declare_global_commands=702417777004380231
            ).add_prefix("$")
        )
        client.load_modules("tamr.commands._loader")
        return client