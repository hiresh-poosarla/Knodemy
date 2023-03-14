import os, discord
from discord.ext import commands
import mimetypes
import requests
from io import BytesIO
from caption import caption_image

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
SUPPORTED_MIMETYPES = ["image/jpeg", "image/png", "image/webp"]

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command(name="caption", brief="Add a caption to an image.", help="""Add a caption to an attached image. Example:
             
!caption "Hello world!" <attached image>

Supported image types: PNG, JPEG, WebP
             """)
async def caption(ctx, caption_text):
    # Must have caption text
    if not caption_text:
        await ctx.message.reply("Please include some caption text after the `!caption` command. For example `!caption \"Hello world!\"")
        return
    
    # Must have a file attached
    if ctx.message.attachments:
        image_url = ctx.message.attachments[0].url
    else:
        await ctx.message.reply("Please attach an image for me to caption.")
        return

    # File must be an image
    if mimetypes.guess_type(image_url)[0] not in SUPPORTED_MIMETYPES:
        await ctx.message.reply("Sorry, the file you attached is not a supported image format. Please upload a PNG, JPEG or WebP image.")
        return

    # Fetch image file
    response = requests.get(image_url)

    # Store image file name
    image_filename = ctx.message.attachments[0].filename

    # Caption image
    final_image = caption_image(BytesIO(response.content), caption_text)

        # Send reply
    await ctx.message.reply(file=discord.File(BytesIO(final_image), filename=f"captioned-{image_filename}"))

bot.run(DISCORD_TOKEN)
