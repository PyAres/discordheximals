# example
import discordheximals


@bot.command()
async def command(ctx):
    embed = discord.Embed(
        title="title",
        description="description",
        color=discordheximals.Color.air_force_blue(),
        timestamp=datetime.datetime.utcnow(),
    )
    await ctx.send(embed=embed)
