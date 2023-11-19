import random, requests,os
import discord
from discord.ext import commands
from envir import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')



#selamlama
@bot.command()
async def selam(ctx):
    await ctx.send(f'selam! ben adeus, senin botunum')

skor=0

#bilgioyunusoru1
@bot.command()
async def s1(ctx):
    await ctx.send(f'Soru 1) Bir pil yaklaşık kaç metrekareyi kirletir?')
    with open(r'images\pil.jpg', 'rb') as f:
         picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def c1(ctx,cevap):
    global skor    
    if int(cevap)==4:
        await ctx.send(f'Doğru:thumbsup:')
        skor+=20
    else: 
        await ctx.send(f'Yanlış:pensive:')
        skor-=20

@bot.command()
async def s2(ctx):
    await ctx.send(f'Soru 1) Bulaşık makinesi kaç litre su tüketir?')
    with open(r'images\bulasikmakinesi.png', 'rb') as f:
         picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def c2(ctx,cevap):
    global skor
    if int(cevap)==10:
        await ctx.send(f'Doğru:thumbsup:')
        skor+=20
    else: 
        await ctx.send(f'Yanlış:pensive:')
        skor-=20

@bot.command()
async def s3(ctx):
    await ctx.send(f'Soru 3) Hangi sera gazı atmosferde en fazla bulunur?')
    with open(r'images\atmosfer.jpg', 'rb') as f:
         picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def c3(ctx,cevap):
    global skor
    if cevap=='CO2':
        await ctx.send(f'Doğru:thumbsup:')
        skor+=20
    else: 
        await ctx.send(f'Yanlış:pensive:')
        skor-=20

@bot.command()
async def s4(ctx):
    await ctx.send(f'Soru 4) Doğaya en çok zarar veren gaz hangisidir?')
    with open(r'images\co2.jpg', 'rb') as f:
         picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def c4(ctx,cevap):
    global skor
    if cevap=="CO2":
        await ctx.send(f'Doğru:thumbsup:')
        skor+=20
    else: 
        await ctx.send(f'Yanlış:pensive:')
        skor-=20

@bot.command()
async def s5(ctx):    
    await ctx.send(f'Soru 5) Bir yılda Dünyada ortalama kaç metreküp su harcanır?')
    with open(r'images\su.jpg', 'rb') as f:
         picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def c5(ctx,cevap):
    global skor
    if int (cevap)>=4000 and int (cevap) <=4500:
        await ctx.send(f'Doğru:thumbsup:')
        skor+=20
    else: 
        await ctx.send(f'Yanlış:pensive:')
        await ctx.send(f'Bir yılda Dünyada ortalama 4000-4500 metreküp su harcanır')
        skor-=20

@bot.command()
async def puan(ctx):
    global skor
    await ctx.send(f'skorunuz={skor}')
    
bot.run(TOKEN)