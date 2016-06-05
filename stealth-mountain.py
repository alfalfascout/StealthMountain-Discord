#!/usr/bin/env python3

"""
A recreation of Stealth Mountain for as a Discord bot
Original Stealth Mountain here: https://twitter.com/stealthmountain
Created by Alan Jacon "alfalfascout"
Using discord.py
"""

import json
import asyncio
import discord
from discord.ext import commands


class StealthMountainBot(commands.Bot):
    @asyncio.coroutine
    def on_message(self, message):
        if message.author = self.user:
            return

        elif "sneak peak" in message.clean_content.lower():
            """ If anybody says sneak peak, let them know """
            yield from self.send_message(message.channel, 'I think you mean "sneak peek".')

        else:
            yield from self.process_commands(message)

""" Set the bot information for login """
description = ("I'm a discord bot based on the original Stealth Mountain: "
    "twitter.com/stealthmountain. I'm one sneaky peak.")
bot = StealthMountainBot(command_prefix=commands.when_mentioned_or('^^'), description=description)
with open('auth.json', 'r') as authfile:
    auths = json.load(authfile)


@bot.event
async def on_ready():
    """ When the bot is up and running, print its username and id
        to the console. """
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(auths["token"])
