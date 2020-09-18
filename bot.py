import discord
from discord.ext import commands
import random
import re


TOKEN = "NjQ4OTAzNjc4NzQ0MzMwMjUy.Xd1ApQ.FobK8XxpCLm20Yb_iHolze0mtoA"  # unique key of discord bot


bot = commands.Bot(command_prefix="diss")


# to match with predefined list of diss
"""with open("diss_list.txt", "r") as fd:
    temp_diss_listk = list(fd.readlines())
    from_list_of_dissk =[]
    for i in temp_diss_listk:
        from_list_of_dissk.append(i.strip())
"""
with open("diss_list.txt", "r") as fd:
    temp_list1 = list(fd.readlines())
    for line in temp_list1:
        line = line.replace("\r", "").replace("\n", "")


def from_list_of_dissk(x):
    y = temp_list1[x]
    return y
    


# to match with predefined list of inputs
with open("input_list.txt", "r") as fi:
    temp_input_listk = list(fi.readlines())
    from_list_of_inputsk = []
    for i in temp_input_listk:
        from_list_of_inputsk.append(i.strip())


# to match with predefined list of regular outputs
with open("input_list.txt", "r") as fo:
    temp_list2 = list(fo.readlines())
    for line in temp_list2:
        line = line.replace("\r", "").replace("\n", "")


def from_list_of_outputsk(x):
    y = temp_list2[x]
    return y


# to read actual commands
class input_msgg:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_cmnnd(self):
        full_cmnnd = "{} {}".format(self.first, self.last)
        return full_cmnnd

    @full_cmnnd.setter
    def full_cmnnd(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last


# main
class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    async def on_message(self, message):

        random.shuffle(temp_list1)  # shiffles diss list

        cmd_prefixx = r"^diss "  # tag_prefixx = r"^@"

        temp_var1 = message.content
        received_msg = temp_var1.lower()

        received_msg_length = len(message.content.split())
        print("number of words in string are : " + str(received_msg_length))

        random_nok = int(random.randint(0, (len(temp_list1))))
        random_msgk = from_list_of_dissk(random_nok)

        # don't respond to ourselves
        if message.author == self.user:
            return

        if (
            re.match(cmd_prefixx, received_msg) and received_msg_length == 2
        ):  # checks whether bot is called or not

            print("message sender id :" + str(message.author.id))

            input_msg_main = input_msgg("xx", "yy")  # CLASS CALLED
            input_msg_main.full_cmnnd = (
                received_msg  # setter called to split prefix and meaningful input
            )
            meaningfull_input = (
                input_msg_main.last
            )  # use meaningfull_input to to take second input

            print("command received :" + str(meaningfull_input))

            if meaningfull_input in from_list_of_inputsk:

                k = from_list_of_inputsk.index(meaningfull_input)
                await message.channel.send(
                    "{0.author.mention} ".format(message) + from_list_of_outputsk(k)
                )
                return

            if len(message.raw_mentions) > 0:

                temp_mentioned_list = message.raw_mentions
                mentioned = str(temp_mentioned_list[0])

                print("member mentioned :" + str(mentioned))
                await message.channel.send("<@!{}> ".format(mentioned) + random_msgk)
                return

            if not meaningfull_input in from_list_of_inputsk:

                await message.channel.send(
                    "{0.author.mention} ".format(message) + random_msgk
                )
                return


client = MyClient()
client.run(TOKEN)

