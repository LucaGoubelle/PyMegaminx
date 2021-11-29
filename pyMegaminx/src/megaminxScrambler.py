import megaminx
from random import randint

class MegaminxScrambler:
    
    def __init__(self):
        self.scrambleList = [
            "D++ R++ D++ R++ D++ R++ D++ R-- D-- R-- U R++ D++ R++ D++ R++ D++ R-- D++ R++ D++ U R++ D-- R++ D-- R-- D++ R-- D-- R++ D-- U' D-- R++ D-- R++ D++ R++ D++ R++ D-- R-- U D-- R++ D++ R-- D-- R++ D++ R-- D++ R++ U' D-- R-- D-- R++ D-- R++ D++ R-- D-- R++ U R-- D++ R-- D++ R-- D++ R++ D-- R-- D++ U'",
            "D-- R++ D-- R++ D++ R-- D-- R++ D-- R-- U R++ D++ R++ D-- R-- D-- R-- D-- R++ D-- U' R++ D++ R++ D-- R++ D-- R++ D++ R++ D++ U D++ R-- D-- R++ D++ R++ D++ R++ D++ R++ U' D-- R-- D++ R++ D++ R++ D++ R++ D++ R++ U' D-- R-- D++ R++ D-- R-- D++ R-- D++ R++ U D-- R-- D++ R++ D++ R++ D++ R-- D-- R-- U'",
            "D++ R-- D-- R-- D-- R-- D-- R-- D++ R++ U' R-- D-- R++ D++ R++ D-- R-- D-- R++ D-- U D-- R++ D-- R++ D++ R-- D++ R++ D-- R++ U D++ R-- D-- R++ D-- R++ D-- R++ D++ R-- U D-- R-- D++ R++ D-- R++ D++ R++ D-- R-- U' D-- R-- D-- R++ D++ R++ D-- R-- D-- R-- U' R++ D-- R-- D-- R-- D++ R-- D-- R-- D++ U",
            "D++ R++ D-- R-- D++ R++ D++ R-- D++ R++ U' R++ D++ R++ D++ R++ D-- R-- D-- R++ D++ U' R++ D++ R-- D-- R-- D++ R-- D-- R-- D-- U D++ R++ D++ R-- D++ R++ D-- R-- D-- R-- U' D-- R++ D-- R++ D-- R++ D-- R-- D-- R-- U' D++ R-- D++ R++ D-- R-- D-- R-- D++ R++ U R-- D-- R-- D++ R++ D-- R-- D++ R-- D++ U'",
            "D-- R++ D++ R++ D++ R++ D-- R-- D++ R-- U R-- D-- R-- D-- R++ D-- R-- D++ R-- D-- U' D-- R++ D++ R++ D++ R++ D-- R-- D++ R-- U R-- D-- R++ D++ R++ D++ R++ D++ R-- D-- U' D-- R++ D-- R++ D-- R++ D-- R++ D++ R-- U D++ R++ D-- R++ D++ R++ D++ R-- D++ R++ U R++ D-- R-- D++ R-- D++ R-- D++ R++ D-- U'",
            
            "D++ R-- D++ R-- D++ R++ D++ R-- D-- R-- U' R++ D-- R-- D-- R++ D-- R++ D-- R-- D-- U' D-- R++ D++ R-- D++ R-- D++ R++ D-- R++ U' D++ R-- D++ R-- D-- R++ D++ R++ D++ R-- U' R-- D++ R++ D++ R++ D++ R-- D++ R++ D++ U D++ R++ D++ R-- D++ R-- D-- R-- D++ R-- U' D++ R++ D-- R++ D++ R++ D++ R++ D++ R-- U",
            "R++ D++ R-- D-- R++ D-- R-- D++ R-- D-- U' D++ R-- D-- R-- D++ R++ D-- R++ D-- R-- U' D-- R-- D++ R-- D++ R-- D-- R++ D-- R-- U' D-- R-- D-- R++ D-- R-- D++ R-- D-- R++ U' D-- R++ D++ R++ D++ R-- D++ R-- D++ R++ U' R-- D-- R++ D++ R-- D-- R-- D-- R-- D++ U D++ R-- D-- R-- D++ R-- D-- R++ D++ R++ U'",
            "R-- D-- R++ D++ R++ D-- R++ D-- R++ D++ U D++ R++ D++ R-- D++ R++ D-- R-- D++ R++ U D-- R++ D++ R-- D-- R++ D-- R-- D-- R++ U' D++ R-- D-- R++ D-- R-- D++ R-- D++ R-- U' D-- R++ D-- R++ D++ R++ D++ R-- D++ R-- U D-- R-- D-- R-- D-- R++ D-- R++ D-- R-- U R++ D-- R-- D-- R++ D++ R++ D-- R-- D-- U'",
            "R++ D++ R-- D++ R-- D-- R-- D++ R-- D-- U' R++ D-- R++ D++ R-- D++ R++ D-- R-- D-- U' D-- R-- D++ R-- D-- R-- D++ R-- D-- R-- U' D++ R-- D++ R++ D-- R++ D++ R-- D++ R++ U' R-- D-- R++ D++ R-- D-- R-- D++ R++ D++ U' D-- R-- D-- R++ D++ R++ D-- R++ D-- R-- U' D++ R-- D++ R-- D++ R++ D++ R-- D-- R-- U'",
            "D-- R-- D-- R-- D++ R++ D++ R++ D-- R++ U D-- R++ D-- R++ D-- R++ D-- R-- D-- R++ U' R-- D++ R++ D++ R++ D++ R-- D++ R-- D++ U' D-- R-- D-- R-- D++ R++ D++ R++ D++ R++ U D++ R-- D++ R-- D++ R++ D++ R-- D-- R-- U' R-- D++ R++ D++ R++ D-- R++ D-- R++ D-- U D++ R-- D-- R-- D-- R++ D-- R-- D++ R-- U"
        ]
        
    def getAllMoves(s):
        return s.split()
    
    def scrambleMegaminx(minx, scramble):
        scrambleLst = MegaminxScrambler.getAllMoves(scramble)
        for mv in scrambleLst:
            if mv=="U" or mv=="U'":
                if mv=="U": minx = minx.move_U()
                elif mv=="U'": minx = minx.move_U_prime()
            elif mv == "R++" or mv == "R--": 
                if mv=="R++": minx = minx.move_RPP()
                elif mv =="R--": minx = minx.move_RMM()
            elif mv=="D++" or mv=="D--":
                if mv=="D++": minx = minx.move_DPP()
                elif mv =="D--": minx = minx.move_DMM()
        return minx
    
    def getScrambledMegaminx(self, minx):
        randomScramble = self.scrambleList[randint(0,len(self.scrambleList)-1)]
        return MegaminxScrambler.scrambleMegaminx(minx, randomScramble)