class Config(object):
      def __init__(self):
          self.BotToken     = '5246743394:AAH8FmXipnGEdEtJGXZYuhq_V-xj2R4R-J8'
          self.api_id = '17768206'
          self.api_hash = 'eedc1c0bdd030dd080e6a300ba942d18'
          self.AdminUsers = 'Luffy15023'
          self.ChunkSizeTel = 2000
          
          self.ChunkSize    = 150
          self.ChunkFixed   = 150
          self.FileLimit    = 1024 * 1024 * 150
          self.ExcludeFiles = ['bot.py','Config.py','multiFile.py','requirements.txt','Procfile','__pycache__','.git','.profile.d','.heroku','bot.session','bot.session-journal','output']
          self.ChunkedFileLimit = 1024 * 1024 * 1024
          self.InProcces = False
          #self.BotChannel = '-1001432878672'
          self.current_user_msg = ''
          self.current_chanel_msg = ''
          self.procesing = False
          self.watching = False
          self.watch_message = []
          self.users = []
          self.userindex = 0
          self.parte= 0
          self.total= 0
          self.totalsub= 0

     

     

      def setChunkSize(self,chunk : int):
          self.ChunkSize = chunk

      def setChunkSizeTel(self,chunk : int):
          self.ChunkSizeTel = chunk

      def toStr(self):
          return '[Chunk Size]\n' + str(self.ChunkSize) + '\n\n[ChunkSizeTel]\n' + str(self.ChunkSizeTel)

      


