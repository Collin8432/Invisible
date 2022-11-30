from .sub.incognito import *
from .sub.setup import *
from .commands.helpcommand import *
from .commands.purgecommand import *
from .commands.verifycommand import *

def setup(bot):
   # Commands
   bot.add_cog(HelpCommand(bot))
   bot.add_cog(PurgeCommand(bot))
   # Sub Commands / Command Groups
   bot.add_cog(Incognito(bot))
   bot.add_cog(Setup(bot))
   bot.add_cog(Verify(bot))
 