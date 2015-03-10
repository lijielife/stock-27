#-*- coding: utf-8 -*-
r"""get data from google finance
"""
import urllib.parse
import urllib.request
import datetime
import time
import csv
import sys

#"http://ichart.yahoo.com/table.csv?s=^TWII&a=2&b=2&c=2014"
#"http://finance.yahoo.com/d/quotes.csv?s=^TWII&f=p0ohgc1"
#p0 - last close value
#o - today open
#h - today high
#g - today low
#c1 - change

class YFClass():
    yfDate=0
    yfStart=1
    yfHigh=2
    yfLow=3
    yfEnd=4
    yfVol=5
    def __init__ (self):
        """constructor

        Args:
        Returns:
        Raises:
        """
        self.stockid="^TWII"
        self.startDateTime=datetime.datetime(1976, 1, 1, 8, 0, 0)
        self.outputFile="hitory.csv"
        self.yahooDateStrType="%Y-%m-%d"
        self.dataStrType="%Y/%m/%d"
    def getHistoryData (self, olist, isymbol=None, isdt=None):
        """get history data from google finance

        Args:
            olist- output data list
            isymbol- stock symbol
            isdt- the date start to get data
        Returns:
        Raises:
            False- no data
            True- data ready
        """
        if isdt!=None:
            self.startDateTime=isdt
        if isymbol!=None:
            self.stockid=isymbol

        dstr=datetime.datetime.strftime(self.startDateTime, self.yahooDateStrType)
        urlstr="http://ichart.yahoo.com/table.csv?s={0:s}&a={1:d}&b={2:d}&c={3:d}".format(
            self.stockid,
            int(dstr[5:7]) - 1,
            int(dstr[8:10]),
            int(dstr[0:4]))
        #print(urlstr)
        try:
            opener = urllib.request.build_opener()
            opener.addheaders = [('User-agent', 'Chrome')]
            content = opener.open(urlstr).read().decode("utf-8").split('\n')
            self.urlData2List(content, olist)
            olist.sort()
            print("ID: {0:s} StartDate: {1:s} DataSize:{2:d}".format(
                self.stockid, datetime.datetime.strftime(self.startDateTime, self.dataStrType), len(olist)))
            #for item in olist:
            #    print(item)
        except urllib.error.HTTPError:
            print("No data")
        return True
    def urlData2List (self, idata, odata):
        """convert google data to data

        Args:
            idata- google input data
            odata- output data
        Returns:
        Raises:
        """
        for icount in range(len(idata)):
            ltemp=idata[icount].split(',')
            try:
                dt = datetime.datetime.fromtimestamp(time.mktime(time.strptime(ltemp[0], self.yahooDateStrType)))
            except ValueError:
                continue
            try:
                openValue=float(ltemp[1].replace(",",""))
            except ValueError:
                openValue=0.0
            try:
                highValue=float(ltemp[2].replace(",",""))
            except ValueError:
                highValue=0.0
            try:
                lowValue=float(ltemp[3].replace(",",""))
            except ValueError:
                lowValue=0.0
            try:
                closeValue=float(ltemp[4].replace(",",""))
            except ValueError:
                closeValue=0.0
            try:
                volValue=float(ltemp[5].replace(",",""))
            except ValueError:
                volValue=0.0
            odata.append([dt, openValue, highValue, lowValue, closeValue, volValue])

    def getLatest2List (self, ilist, isymbol):
        """according list from csv, get lastest data from google finance

        Args:
            ilist- google input data
            isymbol- stock symbol
        Returns:
        Raises:
        """
        if len(ilist)>0:
            lastdt=ilist[len(ilist)-1][0]+datetime.timedelta(days=1)
        else:
            lastdt=datetime.datetime(1985, 1, 1, 0, 0, 0)
        self.getHistoryData(ilist, isymbol, lastdt)
    def csv2list (self, icsvfilename, odata):
        """read csv data into memory

        Args:
            icsvfilename- csv file name
            odata- output data
        Returns:
        Raises:
        """
        try:
            csvFileR=open(icsvfilename, "r")
        except FileNotFoundError:
            return
        csvContent=csv.reader(csvFileR, delimiter=',')
        for i in csvContent:
            dt = datetime.datetime.fromtimestamp(time.mktime(time.strptime(i[0], self.dataStrType)))
            try:
                openValue=float(i[1].replace(",",""))
            except ValueError:
                openValue=0.0
            try:
                highValue=float(i[2].replace(",",""))
            except ValueError:
                highValue=0.0
            try:
                lowValue=float(i[3].replace(",",""))
            except ValueError:
                lowValue=0.0
            try:
                closeValue=float(i[4].replace(",",""))
            except ValueError:
                closeValue=0.0
            try:
                volValue=float(i[5].replace(",",""))
            except ValueError:
                volValue=0.0
            odata.append([dt, openValue, highValue, lowValue, closeValue, volValue])
        odata.sort()
        csvFileR.close()
    def list2csv (self, ocsvfilename, idata):
        """save list data to csv

        Args:
            ocsvfilename- csv file name
            idata- input data
        Returns:
        Raises:
        """
        csvFileW=open(ocsvfilename, "w", newline='')
        csvContent=csv.writer(csvFileW, delimiter=',')
        for icount in range(len(idata)):
            csvContent.writerow([datetime.datetime.strftime(idata[icount][0], self.dataStrType),
                             str(idata[icount][1]),
                             str(idata[icount][2]),
                             str(idata[icount][3]),
                             str(idata[icount][4]),
                             str(idata[icount][5])])
        csvFileW.close
def symbol2Filename (isymbol):
    return symbolstr.replace("^","Index_")+".csv"
if __name__ == "__main__":
    symbollist=["^STI",     #^STI - �s�[�Y���l�ɳ�����
                "^JKSE"]    #^JKSE - �L�����[�F��X���� Jakarta Composite Index
    yfc=YFClass()
    array=[]
    #yfc.getHistoryData(array)
    #yfc.list2csv("temp.csv", array)
    #yfc.csv2list("temp.csv", array)
    for symbolstr in symbollist:
        array=[]
        filename=symbol2Filename(symbolstr)
        print(filename+" processing...")
        sys.stdout.flush()
        yfc.csv2list(filename, array)
        lastlen=len(array)
        yfc.getLatest2List(isymbol=symbolstr, ilist=array)
        newlen=len(array)
        yfc.list2csv(filename, array)
        print("New add {0:d} data".format(newlen-lastlen))
