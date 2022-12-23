from .sub.Invisible import *
from .sub.setup import *
from .sub.website import *
from .commands.helpcommand import *
from .commands.purgecommand import *
from .commands.verifycommand import *

from .task import *

def setup(bot):
   # Commands
   bot.add_cog(HelpCommand(bot))
   bot.add_cog(PurgeCommand(bot))
   # Sub Commands / Command Groups
   bot.add_cog(Invisible(bot))
   bot.add_cog(Setup(bot))
   bot.add_cog(Verify(bot))
   bot.add_cog(Website(bot))
   
   bot.add_cog(Tasks(bot))
 