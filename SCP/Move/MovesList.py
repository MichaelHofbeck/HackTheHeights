#returns dictionary with move name as key and move class as value
from Move import Move
def MoveList():
    ret = dict()
    #student moves
    ret["sigh"] = Move(.89, 5)
    ret["eyeroll"] = Move(.9, 8)
    ret["homework finnesse"] = Move(.75, 25)
    ret["knowledge cram"] = Move(.65, 35)
    #trumpcard
    ret["bitch slap"] = Move(.45, 100)

    #teacher moves
    ret["ramble and shamble"] = Move(.95, 12)
    ret["f*cked HW"] = Move(.65, 30)
    ret["pop quiz"] = Move(.75, 20)
    ret["midterm"] = Move(.50, 25)

    return ret

