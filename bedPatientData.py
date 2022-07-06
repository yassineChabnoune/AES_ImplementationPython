class bedData :

   def __init__(self, id, cardioData,tensionData,  ) :
      self._ID = id
      self._CARDIODATA = cardioData
      self._TENSIONDATA = tensionData
   
   def __getID__(self):
      return self._ID
   def __getCARDIODATA__(self):
      return self._CARDIODATA
   def __getTENSION__(self):
      return self._TENSIONDATA

