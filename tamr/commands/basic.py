import tanjun

COMPONENT = tanjun.Component()

@COMPONENT.with_slash_command
@tanjun.as_slash_command("hello",
                         "Says hello to the bot, mostly to see if bot still alive lmao.",
                         default_to_ephemeral=True)
async def hello(ctx: tanjun.abc.Context):
    await ctx.respond(f"Hi... :flushed:")
