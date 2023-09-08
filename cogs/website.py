import disnake
from disnake.ext import commands, tasks
from env import *
from database import Database



class Website(commands.Cog):



    def __init__(self, bot: commands.Bot):

        self.bot = bot
        print("Cog Website is loaded!")



    @commands.slash_command()
    async def website(self, inter):
        pass



    @website.sub_command(description="Krijg de URL van de ADT&G site!")
    async def url(self, inter):
        await inter.response.send_message("https://alldaytechandgaming.nl/", ephemeral=True)
        


    @commands.default_member_permissions(moderate_members=True)
    @commands.slash_command()
    async def website_bot(self, inter):
        pass



    @website_bot.sub_command(description="Maak een account aan")
    async def maak_account(self, inter, email:str):

        Database.cursor.execute(f"INSERT into discord_auth (email) VALUES ('{email}')")
        Database.db.commit()

        await inter.response.send_message(f"https://alldaybot.alldaytechandgaming.nl/discord/auth?email={email}", ephemeral=True)



def setup(bot: commands.Bot):
    bot.add_cog(Website(bot))