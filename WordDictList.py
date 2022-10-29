appInfo={
    "Canape":{
        "title":"Vector CANape",
        "directory":"C:\\"
    },
    "Notepad":{
        "title":"",
        "directory":""
    },
    "test":{
        "title":"test",
        "directory":"test"
    }
}

appList={
    "기록":appInfo["Canape"],
    "카나페":appInfo["Canape"],
    "로그":appInfo["Canape"],
    "메모":appInfo["Notepad"],
    "메모장":appInfo["Notepad"],
    "적어":appInfo["Notepad"],
    "저거":appInfo["Notepad"],
    "":{
        "title":"",
        "directory":""
    }
}

for targetAudio, key,title,directory in appList:
    print(key)