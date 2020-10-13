#!/usr/bin/env python
import json
from cachetools import cached, LRUCache
import datetime
eceldProjHome = "/home/kali/eceld-netsys/ProjectData/"

@cached(LRUCache(maxsize=1080))
#ProjName = name of the project 
#timeReq = requested time to focus
#context = how many entries to return
#cushion = range of what's considered valid time ... timeReq-cushion >= [valid] < timeReq+cushion
def syncTime(projName,timeReq, context, cushion): #interface for syncing views. 
    datetimeobj = datetime.datetime.strptime(timeReq, "%Y-%m-%dT%H:%M:%S")
    yield getParsedData(projName+"/ecel-export_1599597147/parsed/auditd/auditdData.JSON",datetimeobj,context,cushion), \
        getParsedData(projName+"/ecel-export_1599597147/parsed/pykeylogger/keypressData.JSON",datetimeobj,context,cushion), \
        getParsedData(projName+"/ecel-export_1599597147/parsed/pykeylogger/click.JSON",datetimeobj,context,cushion) 

@cached(LRUCache(maxsize=900))
def getParsedData(files,timeReq,context,cushion):
    relevantEntries=[]
    count=0
    with open(files,"r") as auditfile:
        entries = json.loads(auditfile.read())
        if timeReq==-1:
            return entries
        for entry in entries:
            tempTime = datetime.datetime.strptime(entry["start"], "%Y-%m-%dT%H:%M:%S")
            if tempTime.second>=timeReq.second-cushion and tempTime.second<timeReq.second+cushion :
                relevantEntries.append(entry)
                count = count+1
                if count == context:
                    break #They don't want anymore
            elif relevantEntries: #We passed the timeframe, no need to keep going
                break
    return relevantEntries

if __name__ == "__main__":
    for audits, keypresses, clicks in syncTime("tasasdf","2020-09-08T20:32:23",5,2):
        print(audits)
        print(keypresses)
        print(clicks)