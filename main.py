from keep_alive import keep_alive
import discord
import os
import time
import praw
import asyncio
from asyncio import sleep as s
from itertools import cycle
from random import randint, choice
import discord.ext
from discord.ext.commands.core import _CaseInsensitiveDict
from discord.flags import Intents
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import random
import aiohttp
from aiohttp import request
from PIL import Image
from io import BytesIO
import json
import math
import aiofiles
import wikipedia
from pistonapi import PistonAPI
from os import getenv
from dotenv import load_dotenv
import pytz
import youtube_dl
import requests












game = discord.Game("With Something New")
new_game = discord.Game("With your toys")

snipe_message_author = {}
snipe_message_content = {}

client = commands.Bot(command_prefix = '`', Intents=discord.Intents.all(), case_insensitive = True,
allowed_mentions=discord.AllowedMentions(roles=False, users=True, everyone=False)) 














reddit = praw.Reddit(client_id='LU-gzn7Ae1xOjY9WbNbE3w',
                     client_secret='zj7BFBEZqAiesVsqDiZ7VdTagsXMSg',
                     user_agent='memsbot')








#on online it will change its status
@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=game)


#when message get delete it will log it
@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await s(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]




#bot will shut down
@client.command(name='shutdown' , help = 'shutdown the bot. note only owner of bot can use this command')
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()


    
#change status
@client.command(name = 'change' , help = 'change bot presence')
async def change(ctx):
  await client.change_presence(status=discord.Status.idle, activity=new_game)

  

    
#show server info
@client.command(name = 'serverinfo' , help = 'get server info')
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)




#show latest deleted message
@client.command(name = 'snipe', help = 'check last delete msg')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
        em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")




#do a drop
@client.command(name = 'drop' , help = 'do a drop of a thing')
@commands.has_permissions(manage_messages  = True)
async def drop(ctx, time : str, *, prize: str):

    embed = discord.Embed(title=prize,
                          description=f"Hosted by - {ctx.author.mention}\nReact with :tada: to enter!\nTime Remaining: **{time}** seconds",
                          color=ctx.guild.me.top_role.color, )

    msg = await ctx.channel.send(content=":tada: **GIVEAWAY** :tada:", embed=embed)
    await msg.add_reaction("🎉")
    await asyncio.sleep(3)
    new_msg = await ctx.channel.fetch_message(msg.id)

    user_list = [u for u in await new_msg.reactions[0].users().flatten() if u != client.user] # Check the reactions/don't count the bot reaction

    if len(user_list) == 0:
        await ctx.send("No one reacted.") 
    else:
        winner = random.choice(user_list)
        await ctx.send(f"{winner.mention} You have won the {prize}!")




#show pfp of user
@client.command()
async def avatar(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)





#fbi open up
@client.command(name = 'fbi' , help = 'fbi come to take you')
async def fbi(ctx):
  await ctx.reply('https://tenor.com/view/traffic-fbi-open-up-raid-gif-13450966')





#something special
@client.command(name = 'rr' , help = 'try this')
async def rr(ctx):
  await ctx.send('https://tenor.com/view/rick-astly-rick-rolled-gif-22755440')



#eats vimal and something more
@client.command(name = 'vimal' , help = 'eats vimal')
async def vimal(ctx):
    x=randint(0,1)
    messages=["https://tenor.com/view/vimal-ajay-devgan-drink-gif-15068251", "https://tenor.com/view/rick-roll-gif-19920902"]
    await ctx.send(messages[x])



#die emoji
@client.command(name = 'die' , help = 'send a gun trying to kill you emoji')
async def die(ctx):  
  await ctx.send('<:Die:873898239689105418>')

#addition
@client.command(name = 'add' , help = 'do addtion for ex. :add 4 4')
async def add(ctx, num1:int, num2:int):
  await ctx.reply(num1+num2)


#sub
@client.command(name = 'sub' , help = 'do subtraction for ex. :sub 4 4')
async def sub(ctx, num1:int, num2:int):
  await ctx.reply(num1-num2)

#div
@client.command(name = 'div' , help = 'do division for ex. :div 4 4')
async def div(ctx, num1:int, num2:int):
  await ctx.reply(num1/num2)

#mul
@client.command(name = 'mul' , help = 'do multiplication for ex. :mul 4 4')
async def mul(ctx, num1:int, num2:int):
  await ctx.reply(num1*num2)


#motivate alot
@client.command(name = 'motivate' , help = 'kinda help to make your pain more painfull')
async def motivate(ctx):
    embed=discord.Embed(title="you are alone",  description="life sucks", color=0xFF5733)
    await ctx.send(embed=embed)


#kick member
@client.command(aliases=['k'],name = 'kick' , help = 'kick member only for admin')
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,*,reason= "idk why they kick his/her they didnt tell me :sob:"):
  await member.send(member.name + "has been kick idk i am a wip bot, they got kick cause:"+reason)
  await member.kick(reason=reason)



@client.command(aliases=['b'],name = 'ban' , help = 'ban member only from admin')
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*,reason= "idk why they kick his/her they didnt tell me :sob:"):
  await member.send(member.name + "has been ban idk i am a wip bot, they got ban cause:"+reason)
  await member.ban(reason=reason)
























@client.command(name = 'meme' , help = 'send meme')
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 10)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
























@client.command(name = 'settimer' , help = 'set a timer only work with min sorry for it')
async def settimer(ctx, minutes , * , mgg):
    try:
        minutes = int(minutes)
        if minutes < 1:
            await ctx.send("Please define time more or equal than 1 minute.")
            return
        seconds = minutes * 60
        count_min = math.floor(seconds / 60)
        count_sec = seconds % 60
    except:
        await ctx.send("Please enter a valid number.")
        return
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
        message = await ctx.send(f"Timer: {count_min}:{count_sec}")
    while True:
        seconds -= 1
        count_min = math.floor(seconds / 60)
        count_sec = seconds % 60
        if seconds == 0:
            await message.edit(content="Timer Ended!")
            break
        if len(str(count_sec)) == 1:
            count_sec = f"0:{count_sec}"
            await message.edit(content=f"Timer: {count_min}:{count_sec}")
        else:
            await message.edit(content=f"Timer: {count_min}:{count_sec}")
            await asyncio.sleep(1)
    await ctx.send(f"{ctx.author.mention}, Your timer of {mgg} is done!")



@client.command(name = 'searchwiki' , help = 'do a wiki search')
async def searchwiki(ctx, search_text):
    defintion = wikipedia.summary(search_text)
    embed = discord.Embed(title="Searching....", description=defintion, color=discord.Colour.purple())
    await ctx.send(embed=embed)
  


@client.command(name = 'dog' , help = 'send fact and pic of dog')
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
      # This time we'll get the fact request as well!
      request2 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request2.json()

   embed = discord.Embed(title="Doggo!", color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)












@client.command(name = 'cat' , help = 'send fact and pic of cat')
async def cat(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat')
      dogjson = await request.json()
      # This time we'll get the fact request as well!
      request2 = await session.get('https://some-random-api.ml/facts/cat')
      factjson = await request2.json()

   embed = discord.Embed(title="meoowwww!", color=discord.Color.purple())
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)













@client.command(name = 'clear' , help = 'clear message ex. :clear 5 that will clear 5 mesage')
@has_permissions(manage_roles=True, ban_members=True)
async def clear(ctx, amount=5):
  await ctx.channel.purge(limit=amount)









  
 
@client.command(name = 'ask' , help = 'bot will tell you yes or no ex.:ask this is best bot?')
async def ask(ctx, *, arg):
    x = randint(0,6)
    messages = ["Im gonna go with yes.", 
                "I mean, I could go either way, but yea I guess.", 
                "TBH idk mate.", 
                "Please stop asking me questions. Geez.", 
                "Nah, I'm feeling no on this one.", 
                "Yea whatever. If I say yes will you be happy?", 
                "Are you serious? Of course not."]
    await ctx.send(messages[x])


@client.command(name = 'print' , help = 'print what you say')
async def print(ctx, arg):
	await ctx.channel.send(arg)


@client.command(name = 'covid' , help = 'tell covid stat ex. :covid usa   . only work for country')
async def covid(ctx, arg):
  await ctx.channel.send(f'https://covid-img.herokuapp.com/country/{arg}')













@client.command(name = 'calc' , help = 'calculate')
async def calc(ctx):
    def check(m):
        return len(m.content) >= 1 and m.author != client.user

    await ctx.send("Number 1: ")
    number_1 = await client.wait_for("message", check=check)
    await ctx.send("Operator: ")
    operator = await client.wait_for("message", check=check)
    await ctx.send("number 2: ")
    number_2 = await client.wait_for("message", check=check)
    try:
        number_1 = float(number_1.content)
        operator = operator.content
        number_2 = float(number_2.content)
    except:
        await ctx.send("invalid input")
        return
    output = None
    if operator == "+":
        output = number_1 + number_2
    elif operator == "-":
        output = number_1 - number_2
    elif operator == "/":
        output = number_1 / number_2
    elif operator == "*":
        output = number_1 * number_2
    else:
        await ctx.send("invalid input")
        return
    await ctx.send("Answer: " + str(output))

@client.command(name = 'flip' , help = 'flip a coin')
async def flip(ctx):
    x=randint(0,1)
    messages=["HEADS\nhttps://tenor.com/view/heads-coinflip-flip-a-coin-coin-coins-gif-21479854", "TAILS\nhttps://tenor.com/view/coins-tails-coin-flip-a-coin-coinflip-gif-21479856"]
    await ctx.send(messages[x])

@client.command(name = 'roll' , help = 'ex. :roll 5')
async def roll(ctx, arg):
    x=randint(1,int(arg))
    await ctx.send(f"You rolled a {x}")






















player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(name='tictactoe', aliases=['ttt', 'tic'] ,  help = 'play tictactoe with friend do :ttt @firstplater @secondplayer  . do :place 5 it will place your mark at 5th slot in grid')
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command(name = 'place' , help = 'do :place 6 it will place youe ttt mark')
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")









@client.command(name = 'play' , help = 'do :play <youtube url> <channel_name>')
async def play(ctx, url : str, channel):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command(name = 'leave' , help = 'leave the voice channel')
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command(name = 'pause' , help = 'pause music playing')
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command(name = 'resume' , help = 'resume paused music')
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command(name = 'stop' , help = 'stop playing music')
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()





r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=e59d4b0ab7c144b1bdf23e66b8f51d31')

r.content

data = json.loads(r.content)

data['articles'][0]
data['articles'][0]['title']
data['articles'][0]['description']
data['articles'][0]['url']
data['articles'][0]['content']


@client.command()
async def news(ctx):
  for i in range(10):
    News = data['articles'][i]['title']
    await ctx.send(f'```{News}```')

@client.command()
async def newsd(ctx):
  for i in range(10):
    News = data['articles'][i]['description']
    await ctx.send(f'```{News}```')


@client.command()
async def newsu(ctx):
  for i in range(10):
    News = data['articles'][i]['url']
    await ctx.send(f'```{News}```')












keep_alive()
client.run(getenv('TOKEN'))