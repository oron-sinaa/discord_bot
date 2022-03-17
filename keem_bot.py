import env
import discord
import random
import requests

client = discord.Client()

greet_words = ["!hi", "!hoi", "!hello", "!hey", "!hola", "!wassup"]
greet_messages =   ["We're happy to have you here!",
                    "Glad to see you!", 
                    "Happy to have you!",
                    "Enjoy the journey with us!", 
                    "May you shine here!",
                    "You added a shine to the server!",
                    "Welcome to the family!",
                    "You look great today! Just like the server.",
                    "Are you a diamond? The server shines brighter now!",
                    "Are you an answer? We were looking for you!"]

@client.event
async def on_ready():
    print("logged in as \"{0.user.name}\" with id {0.user.id}.".format(client))

@client.event
async def on_message(message):
    print("DEBUG: A message was recieved.")
    # ignore if message is from the bot itself
    if message.author == client.user:
        return
   
    # bot greeting replies
    if message.content.lower() in greet_words:
        print("DEBUG: Replying to greeting...")
        random_greet = random.choice(greet_words)[1:]
        await message.channel.send(random_greet.title() + '!')

    # bot quote reply
    if message.content.startswith("!quote"):
        print("DEBUG: Sending a quote...")
        url = "https://zenquotes.io/api/random/"
        response = requests.get(url)
        result = response.json()
        quote = result[0]['q'] + "\n-" + result[0]['a']
        await message.channel.send(quote)

@client.event
async def on_member_join(member):
    print("DEBUG: A member called " + member.name + " joined.")
    embed = discord.Embed(  title = "Welcome " + member.name+"!",
                            description = random.choice(greet_messages), 
                            color = discord.Color.dark_teal()  )

@client.event
async def on_member_leave(member):
    print("DEBUG: A member called " + member.name + " left.")
    embed = discord.Embed(  title = "Goodbye " + member.name + ":'(",
                            description = "Until we meet again...", 
                            color = discord.Color.dark_red()  )

client.run(TOKEN)