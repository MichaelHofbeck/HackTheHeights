#returns dictionary with move name as key and move class as value
from shutil import move
from SCP.Move.Move import Move
def MoveList():
    ret = dict()
    #student moves
    ret["sigh"] = Move(.89, 5)
    ret["eyeroll"] = Move(.9, 8)
    ret["slam table"] = Move(.85, 16)
    ret["homework finnesse"] = Move(.75, 25)
    ret["knowledge cram"] = Move(.9, 35)
    ret["jumping kick"] = Move(.80, 20)
    ret["water gun"] = Move(.9, 7)
    ret["hypnosis"] = Move(.85, 24)
    ret["rage"] = Move(1, 6)
    ret["lovely kiss"] = Move(.9, 30)
    ret["scary face"] = Move(1, 6)
    ret["charm"] = Move(1, 10)
    ret["bitch slap"] = Move(1, 100)

    #teacher moves
    ret["ramble and shamble"] = Move(.95, 12)
    ret["f*cked HW"] = Move(.85, 30)
    ret["body slam"] = Move(.70, 15)
    ret["pop quiz"] = Move(.85, 20)
    ret["midterm"] = Move(.8, 25)

    ret["homework assist"] = Move(.9, -10)
    ret["tbh idk"] = Move(.9, 12)
    ret["squirt"] = Move(.85, 8)
    ret["tackle"] = Move(.65, 17)
    ret["growl"] = Move(1, 5)
    ret["smash latop"] = Move(.9, 25)
    

    return ret

def moveType(type = "user"):
    if type == "user":
        moves = ["sigh", "eyeroll","slam table","homework finnesse","knowledge cram",
        "jumping kick","water gun","hypnosis","rage","lovely kiss","scary face","charm", "growl", "bitch slap"]
    elif type == "teacher":
        moves = ["sigh", "eyeroll","slam table","jumping kick","water gun","hypnosis","rage"
        ,"ramble and shamble", "f*cked HW", "body slam", "pop quiz", "midterm","scary face","charm"]
    else:
        moves = ["homework assist", "tbh idk", "squirt", "tackle", "growl", "sigh", "eyeroll","slam table",
        "jumping kick","water gun","smash laptop","rage","scary face","charm", "growl"]


    return moves

