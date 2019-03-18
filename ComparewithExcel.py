import pandas as pd
import json
import xlsxwriter
class ComparewithExcel:
    def extractvalues(self):
        df = pd.ExcelFile('C:\\Users\\murali\\PycharmProjects\\untitled\\Utilities\\ExcelTrack.xlsx').parse(
            'Sheet1')  # you could add index_col=0 if there's an index
        x = []
        x.append(df['consessionnum'])
        #conNo = x[0].values
        #return conNo

    def insertValues(self, carddata):
        #df1=json.dumps(carddata)
        data=carddata.__dict__
        print(data)
        df = pd.DataFrame(data,index=[0])
        print(df.__dict__)
        writer = pd.ExcelWriter('C:\\Users\\murali\\PycharmProjects\\untitled\\Utilities\\ExcelTrack.xlsx',engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        value = writer.save()
        return value


