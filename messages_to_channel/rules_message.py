import discord


def rules_message():
    rules_list = ['No insulting players, humiliating, threatening, harassing, intimidation, coercion./Zakaz obrażania graczy, poniżania, gróźb, nękania,zastraszanie, zmuszanie.',
        'It is forbidden to clutter the chat (flood, spam, typing in capslock,spamming, swearing)./Zakaz zaśmiecania chatu (flood, spam, pisanie capslockiem, spamowanie, przeklinanie).',
        'No swearing, disturbing or insulting others voice channels./Zakaz przeklinania, przeszkadzania lub obrażania innych osób kanały głosowe.',
        'Prohibition of advertising other servers, sites, forums, etc./Zakaz reklamowania innych serwerów, stron, forów itp.',
        'Prohibition of impersonating the administration and players./Zakaz podszywania się pod administrację i graczy.']
    embed = discord.Embed(title="Rules/Regulamin", description="Każde nieprzestrzeganie zasad może skutkować kickiem lub banem.", color=0xff0000)
    i = 0
    for rule in rules_list:
        embed.add_field(name=f"{i+1}. {rule}", value="\u200b", inline=True)
        i += 1

    return embed

