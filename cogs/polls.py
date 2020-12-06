from discord.ext import commands

# The poll class features the create_poll command, an internal Poll class that stands for a single poll
#   and a map of poll names against polls.
class Polls(commands.Cog):

    # ----- Poll -----
    class Poll:
        def __init__(self, options):
            self.options = {}
            for option in options:
                self.options[option] = []

        def add_member_to_option(self, member, option):
            self.options[option].append(member)

        def remove_member_from_option(self, member, option):
            self.options[option].remove(member)

    # ----- /Poll -----                

    def __init__(self, bot):
        self.bot = bot
        self.polls = {} # K: pollname: str, V: poll: Poll

    @commands.command()
    async def create_poll(self, ctx): # TODO
        args:list = ctx.args
        name = args.pop(0)
        self.polls[name] = self.Poll(args)
        ctx.send(self.get_poll_as_embed(name))

    @commands.command()
    async def close_poll(self, ctx): # TODO
        args:list = ctx.args

    @commands.command()
    async def remove_poll(self, ctx): # TODO
        args:list = ctx.args
        name = args.pop(0)
        self.polls[name] = self.Poll(args)


    def get_poll_as_embed(self, name): # TODO build an embed out of a poll
        return None
    
        
    async def vote(self, ctx): # TODO
        name = ctx.args[0]
        vote = ctx.args[1]
        if name in self.polls.keys and vote in self.polls[name]:
            self.polls[name][vote].append(ctx.author)


