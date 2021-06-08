import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='$')


# print to the console when the bot logs in
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


# handle errors through discord.py. can catch all errors in the bot's commands
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing arguments.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to use this command.')


# send a message to #general when a member joins
@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if channel.name == 'welcome':
            await channel.send(f'{member} has joined the server!')


# assign a role to the user
@client.command()
async def role(ctx, arg: discord.Role):
    if arg in ctx.author.roles:
        await ctx.message.author.remove_roles(arg)
        await ctx.send(f'Removed {arg} from {ctx.author}!')
        print('Role removed')
    else:
        await ctx.message.author.add_roles(arg)
        await ctx.send(f'Gave {ctx.author} the {arg} role!')
        print('Role added')


# list available roles to give to the user
@client.command()
async def listroles(ctx):
    roles = ctx.guild.roles
    role_list = ''
    for i in roles:
        if i.name == '@everyone':
            continue
        if i.name == 'Admin':
            continue
        if i.name == 'Root':
            continue
        role_list += i.name + '\n'
    await ctx.send('These are the available roles (Certain roles will be too high to assign): \n>>> ' + role_list)


# tell the user how long they have been on the server
@client.command()
async def howlong(ctx):
    guild_name = str(ctx.guild.name)
    join_time = str(ctx.author.joined_at)
    fmt = 'You joined {} on {}'
    await ctx.send(fmt.format(guild_name,join_time))


# roll a die of a specified number of sides
@client.command()
async def roll(ctx, sides: int):
    if sides > 0:
        dice = str(random.randint(1, sides))
        await ctx.send('You rolled a ' + dice + '.')
    else:
        await ctx.send('Invalid number of sides!')


# clear up to 5 messages from the channel
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    if amount <=5:
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send('I don\'t think you need to clear that many lines.')


# flip a coin
@client.command()
async def coinflip(ctx):
    coin = random.randint(0,1)
    if coin == 0:
        await ctx.send('Coin landed on heads.')
    else:
        await ctx.send('Coin landed on tails')


client.run('NjMwNTU4MjQwODg3MDEzMzc2.XZqDtw.WkvoW6qTIxK4jKOnMIpPExEca40')