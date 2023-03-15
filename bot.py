import discord
import random

def run_discord_bot():
  TOKEN = 'MTA2Mjk2MjA4NDMwNTk3MzI4OA.GXZZQi.3tVqHbpHHtJ136OrhfMDYVpI_AQx7SvC-XfP1A' #enter token
  intents = discord.Intents.default()
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def on_ready():
     print(f'{client.user} is now running!')
  
  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    # IN THE FOLLOWING CODE, CHOOSE WHAT MATH FUNCTION YOUR CODE WILL DO
    if message.content.startswith('!{BLANK}'):
        nums = message.content.split()[1:]
        if len(nums) != 2:
            await message.channel.send('Please provide 2 numbers.')
            return

        try:
            num1 = float(nums[0])
            num2 = float(nums[1])
        except ValueError:
            await message.channel.send('Please provide valid numbers.')
            return

        result = num1 {CHOOSE AN OPERATOR} num2
        await message.channel.send(f'The {BLANK} of {num1} and {num2} is {result}.')

      #RANDOM FUNCTION, CHOOSE THE PARAMATERS OF THE RANDOM NUMBER YOU WANT TO GENERATE
      if message.content.startswith('!random'):
        await message.channel.send(random.randint({BLANK}))

      #DEFINE FUNCTION BELOW IS A SAMPLE, CREATE AN ADDITIONAL 5-10 MATH WORDS THAT YOU WILL RESEARCH AND DEFINE
      if message.content.startswith('!define function'):
        await message.channel.send("A function in mathematics is an expression, rule, or law that defines a relationship between one variable (the independent variable) and another variable (the dependent variable).")
  
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f'{username} said: "{user_message}" ({channel})')
  
  
  client.run(TOKEN)
