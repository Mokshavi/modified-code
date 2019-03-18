from simple.Scrapy import Scrapy
from simple.DataObject import DataObject
from simple.ComparewithExcel import ComparewithExcel
from simple.Service import Service
class MainClass:
 s = Scrapy()
 carddata = s.card_details_data()
 serviceVo=DataObject().dataobjectcreation(carddata)
 excel=ComparewithExcel()
 conNo=excel.extractvalues()
 try:
   for i in conNo:
    if (carddata['customId_ConsessionNo']!=i):
     dt = DataObject()
     dataobject = dt.dataobjectcreation(carddata)
 except:
   pass
 update=excel.insertValues(serviceVo)
 print(update)






