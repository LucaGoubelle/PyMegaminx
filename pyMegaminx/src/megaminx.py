import pygame

class Color:
    white = (255,255,255)
    yellow = (255,255,0)
    blue = (0,0,255)
    red = (255,0,0)
    green = (0,140,0)
    
    lime = (0,255,0)
    cyan = (0,255,255)
    pink = (255,127,237)
    orange = (255,100,0)
    beige = (255,240,170)
    
    purple = (178,0,255)
    grey = (160,160,160)

class Sticker:
    def __init__(self, c):
        self.color = c
        if self.color == "white":
            self.sprite = Color.white
        elif self.color == "yellow":
            self.sprite = Color.yellow
        elif self.color == "blue":
            self.sprite = Color.blue
        elif c == "red":
            self.sprite = Color.red
        elif c == "green":
            self.sprite = Color.green
        elif c == "purple":
            self.sprite = Color.purple
            
        elif c == "orange":
            self.sprite = Color.orange
        elif c == "cyan":
            self.sprite = Color.cyan
        elif c == "beige":
            self.sprite = Color.beige
        elif c == "pink":
            self.sprite = Color.pink
        elif c == "lime":
            self.sprite = Color.lime
        elif c == "grey":
            self.sprite = Color.grey

class FaceUtils3:
    
    @staticmethod
    def rotate(face):
        nf = [None for i in range(len(face))]
        
        nf[0] = face[8]
        nf[1] = face[9]
        nf[2] = face[0]
        nf[3] = face[1]
        nf[4] = face[2]
        
        nf[5] = face[3]
        nf[6] = face[4]
        nf[7] = face[5]
        nf[8] = face[6]
        nf[9] = face[7]
        nf[10] = face[10]
        
        return nf
    
    @staticmethod
    def rotateAsync(face):
        nf = [None for i in range(len(face))]
        
        nf[0] = face[2]
        nf[1] = face[3]
        nf[2] = face[4]
        nf[3] = face[5]
        nf[4] = face[6]
        
        nf[5] = face[7]
        nf[6] = face[8]
        nf[7] = face[9]
        nf[8] = face[0]
        nf[9] = face[1]
        nf[10] = face[10]
        
        return nf
    
    @staticmethod
    def rotateTwice(face):
        nf = FaceUtils3.rotate(face)
        return FaceUtils3.rotate(nf)
    
    @staticmethod
    def rotateTwiceAsync(face):
        nf = FaceUtils3.rotateAsync(face)
        return FaceUtils3.rotateAsync(nf)
    
    @staticmethod
    def rotateThree(face):
        nf = FaceUtils3.rotate(face)
        nff = FaceUtils3.rotate(nf)
        return FaceUtils3.rotate(nff)
    
    @staticmethod
    def rotateThreeAsync(face):
        nf = FaceUtils3.rotateAsync(face)
        nff = FaceUtils3.rotateAsync(nf)
        return FaceUtils3.rotateAsync(nff)

    @staticmethod
    def transfert(face):
        nf = [None for i in range(len(face))]
        for i in range(len(face)):
            nf[i] = face[i]
        return nf



















class Megaminx:

    dim3d = {
        "up":[
            [(248,70), (285,82), (253,91), (244,91), (211,81)],
            [(297,84), (303,86), (290,104), (262,95)],
            [(312,89), (353,103), (341,122), (301,107), (301,104)],
            [(292,112), (298,112), (333,122), (333,126), (288,127), (284,126)],
            [(284,131), (329,132), (317,151), (266,151), (276,134)],
            [(263,129), (265,132), (253,150), (244,150), (230,132), (232,129)],
            [(210,130), (219,134), (232,149), (181,151), (165,130)],
            [(197,112), (209,123), (205,126), (161,126), (159,122), (192,113)],
            [(179,89), (194,103), (194,106), (162,117), (156,117), (142,99)],
            [(198,84), (231,93), (232,96), (213,102), (204,101), (191,85)],
            [(255,100), (279,110), (279,113), (267,124), (260,126), (232,126), (221,123), (210,111), (236,100)]
        ],
        "front":[
            [(179,163), (228,162), (230,167), (218,203), (207,212), (167,212), (164,208)],
            [(244,163), (251,163), (266,205), (261,211), (234,211), (228,206)],
            [(268,163), (316,163), (332,209), (328,212), (288,212), (276,203), (264,168)],
            [(290,223), (332,223), (338,230), (297,258), (291,253), (284,228)],
            [(333,245), (337,245), (355,290), (317,320), (311,319), (298,282), (301,270)],
            [(282,282), (289,286), (303,328), (296,334), (257,307), (257,298)],
            [(238,312), (249,312), (283,335), (283,340), (243,369), (203,342), (203,337)],
            [(208,280), (230,296), (229,304), (192,331), (185,326), (200,281)],
            [(148,243), (153,243), (186,266), (189,280), (176,316), (169,316), (134,289), (134,285)],
            [(156,221), (203,221), (208,226), (197,257), (190,257), (154,230)],
            [(232,221), (260,221), (273,232), (281,257), (279,270), (250,290), (238,290), (210,266), (209,254), (220,228)],
        ],
        "left":[
            [(131,108), (144,125), (119,158), (107,142)],
            [(147,132), (149,134), (133,178), (124,168), (124,163)],
            [(153,141), (167,159), (152,205), (149,205), (139,190), (139,180)],
            [(131,200), (134,200), (146,217), (143,225), (121,232), (121,226)],
            [(136,237), (136,241), (122,284), (100,292), (101,286), (112,252), (118,244)],
            [(106,249), (107,253), (95,289), (90,294), (91,258), (93,253)],
            [(82,255), (86,258), (85,290), (81,296), (64,301), (66,262)],
            [(85,216), (88,216), (87,238), (82,245), (66,250), (67,243)],
            [(91,164), (90,196), (85,207), (68,231), (70,195)],
            [(102,150), (112,164), (111,171), (97,189), (98,155)],
            [(114,178), (118,178), (125,188), (124,201), (116,226), (109,236), (99,240), (94,236), (95,209), (100,196)]
        ],
        "right":[
            [(340,140), (356,183), (356,190), (345,207), (327,161)],
            [(346,132), (369,165), (369,169), (361,179), (344,134)],
            [(366,112), (386,143), (386,147), (376,162), (355,132), (355,128)],
            [(392,154), (396,161), (397,195), (394,195), (383,178), (383,169)],
            [(399,166), (418,196), (421,234), (404,209), (400,196)],
            [(403,214), (423,242), (423,248), (407,242), (402,234), (401,216)],
            [(406,251), (423,256), (427,297), (409,293), (405,288), (403,254)],
            [(383,249), (394,252), (398,258), (399,295), (396,295), (381,254)],
            [(353,240), (369,245), (376,253), (388,286), (388,293), (366,287), (350,243)],
            [(359,201), (370,228), (370,234), (352,228), (346,220)],
            [(372,179), (376,179), (392,202), (396,215), (396,237), (392,241), (383,239), (377,233), (365,200), (365,190)]    
        ],
        "downLeft":[
            [(127,299), (167,328), (151,335), (146,335), (105,307)],
            [(178,335), (186,340), (187,361), (182,361), (159,345), (158,341)],
            [(194,350), (232,375), (236,379), (236,400), (202,377), (195,368)],
            [(200,381), (237,407), (237,411), (203,398), (198,393), (197,382)],
            [(203,402), (235,414), (239,418), (239,436), (200,420), (199,404)],
            [(163,387), (184,396), (189,402), (189,418), (183,416), (161,390)],
            [(112,368), (141,379), (153,387), (172,411), (136,398)],
            [(116,350), (122,352), (138,373), (107,361), (101,355)],
            [(89,309), (112,338), (112,342), (98,347), (93,346), (69,316)],
            [(99,307), (134,333), (136,337), (124,341), (118,337), (95,309)],
            [(143,345), (151,346), (182,368), (188,376), (188,386), (183,389), (158,380), (149,373), (133,354), (133,348)]
        ],
        "downRight":[
            [(360,301), (382,306), (382,308), (345,334), (336,335), (321,331)],
            [(389,309), (392,310), (367,340), (353,338), (353,335)],
            [(400,306), (422,310), (397,342), (379,339), (379,334)],
            [(371,347), (390,351), (387,356), (357,369), (354,366), (367,350)],
            [(379,365), (356,394), (322,409), (340,385), (350,377)],
            [(329,387), (329,391), (307,416), (302,416), (302,399), (308,395)],
            [(287,402), (294,404), (294,417), (290,422), (257,436), (253,433), (253,416)],
            [(288,380), (293,380), (293,392), (287,397), (252,410), (252,407)],
            [(287,351), (292,351), (292,368), (286,375), (255,399), (251,399), (250,379)],
            [(308,339), (329,342), (329,346), (308,362), (302,362), (303,343)],
            [(342,346), (354,348), (357,354), (343,371), (330,380), (312,387), (302,387), (302,376), (310,366), (331,350)]
        ]
    }
    
    def __init__(self, **kwargs):
        if kwargs["full"] == True:
            self.up = []
            self.front = []
            self.left = []
            self.right = []
            self.downRight = []
            self.downLeft = []
            self.absLeft = []
            self.absRight = []
            self.down = []
            self.backLeft = []
            self.backRight = []
            self.back = []
            
            for i in range(11):
                self.up.append(Sticker("grey"))
            for i in range(11):
                self.front.append(Sticker("pink"))
            for i in range(11):
                self.left.append(Sticker("lime"))
            for i in range(11):
                self.right.append(Sticker("beige"))
            for i in range(11):
                self.downRight.append(Sticker("red"))
            for i in range(11):
                self.downLeft.append(Sticker("blue"))
            for i in range(11):
                self.absLeft.append(Sticker("yellow"))
            for i in range(11):
                self.absRight.append(Sticker("green"))
            for i in range(11):
                self.down.append(Sticker("white"))
            for i in range(11):
                self.backLeft.append(Sticker("orange"))
            for i in range(11):
                self.backRight.append(Sticker("cyan"))
            for i in range(11):
                self.back.append(Sticker("purple"))
        else:
            self.up = kwargs["up"]
            self.front = kwargs["front"]
            self.left = kwargs["left"]
            self.right = kwargs["right"]
            self.downRight = kwargs["downRight"]
            
            self.downLeft = kwargs["downLeft"]
            self.absLeft = kwargs["absLeft"]
            self.absRight = kwargs["absRight"]
            self.down = kwargs["down"]
            self.backLeft = kwargs["backLeft"]
            
            self.backRight = kwargs["backRight"]
            self.back = kwargs["back"]

    def sleeper(t):
        # t = millisecond
        pygame.time.wait(t)
    
    def drawMegaminx(self, scr):
        pygame.draw.polygon(scr, (0,0,0), [
            (248,68),
            (133,100),
            (68,193),
            (62,311),
            (134,400),
            (247,442),
            (356,399),
            (429,305),
            (420,195),
            (363,104)
        ])
        for i in range(11):
            pygame.draw.polygon(scr, self.up[i].sprite, Megaminx.dim3d["up"][i])
        for i in range(11):
            pygame.draw.polygon(scr, self.front[i].sprite, Megaminx.dim3d["front"][i])
        for i in range(11):
            pygame.draw.polygon(scr, self.left[i].sprite, Megaminx.dim3d["left"][i])
        for i in range(11):
            pygame.draw.polygon(scr, self.right[i].sprite, Megaminx.dim3d["right"][i])
        for i in range(11):
            pygame.draw.polygon(scr, self.downLeft[i].sprite, Megaminx.dim3d["downLeft"][i])
        for i in range(11):
            pygame.draw.polygon(scr, self.downRight[i].sprite, Megaminx.dim3d["downRight"][i])
        
        pygame.display.update()

    def multiMove(self, scr, s, delay=200):
        lstMove = s.split(" ")
        for i in range(len(lstMove)):
            if(lstMove[i]=="U" or lstMove[i]=="U'" or lstMove[i]=="U2" or lstMove[i]=="U2'" or lstMove[i]=="U3" or lstMove[i]=="U3'"):
                if(lstMove[i]=="U"):
                    self = self.move_U()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="U'"):
                    self = self.move_U_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="U2"):
                    self = self.move_U2()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="U3"):
                    self = self.move_U3()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="U2'"):
                    self = self.move_U2_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="U3'"):
                    self = self.move_U3_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
            if(lstMove[i]=="F" or lstMove[i]=="F'" or lstMove[i]=="F2" or lstMove[i]=="F2'" or lstMove[i]=="F3" or lstMove[i]=="F3'"):
                if(lstMove[i]=="F"):
                    self = self.move_F()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="F'"):
                    self = self.move_F_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="F2"):
                    self = self.move_F2()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="U3"):
                    self = self.move_U3()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="F2'"):
                    self = self.move_F2_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="F3'"):
                    self = self.move_F3_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
            if(lstMove[i]=="R" or lstMove[i]=="R'" or lstMove[i]=="R2" or lstMove[i]=="R2'" or lstMove[i]=="R3" or lstMove[i]=="R3'"):
                if(lstMove[i]=="R"):
                    self = self.move_R()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="R'"):
                    self = self.move_R_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="R2"):
                    self = self.move_R2()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="R3"):
                    self = self.move_R3()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="R2'"):
                    self = self.move_R2_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="R3'"):
                    self = self.move_R3_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
            if(lstMove[i]=="L" or lstMove[i]=="L'" or lstMove[i]=="L2" or lstMove[i]=="L2'" or lstMove[i]=="L3" or lstMove[i]=="L3'"):
                if(lstMove[i]=="L"):
                    self = self.move_L()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="L'"):
                    self = self.move_L_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="L2"):
                    self = self.move_U2()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="L3"):
                    self = self.move_L3()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="L2'"):
                    self = self.move_L2_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="L3'"):
                    self = self.move_L3_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
            if(lstMove[i]=="D" or lstMove[i]=="D'" or lstMove[i]=="D2" or lstMove[i]=="D2'" or lstMove[i]=="D3" or lstMove[i]=="D3'"):
                if(lstMove[i]=="D"):
                    self = self.move_D()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="D'"):
                    self = self.move_D_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="D2"):
                    self = self.move_D2()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="D3"):
                    self = self.move_D3()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="D2'"):
                    self = self.move_D2_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="D3'"):
                    self = self.move_D3_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
            if(lstMove[i]=="DL" or lstMove[i]=="DL'" or lstMove[i]=="DL2" or lstMove[i]=="DL2'" or lstMove[i]=="DL3" or lstMove[i]=="DL3'"):
                if(lstMove[i]=="DL"):
                    self = self.move_DL()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DL'"):
                    self = self.move_DL_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DL2"):
                    self = self.move_DL2()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DL3"):
                    self = self.move_DL3()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DL2'"):
                    self = self.move_DL2_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DL3'"):
                    self = self.move_DL3_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
            if(lstMove[i]=="DR" or lstMove[i]=="DR'" or lstMove[i]=="DR2" or lstMove[i]=="DR2'" or lstMove[i]=="DR3" or lstMove[i]=="DR3'"):
                if(lstMove[i]=="DR"):
                    self = self.move_DR()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DR'"):
                    self = self.move_DR_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DR2"):
                    self = self.move_DR2()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DR3"):
                    self = self.move_DR3()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DR2'"):
                    self = self.move_DR2_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="DR3'"):
                    self = self.move_DR3_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
            if(lstMove[i]=="BL" or lstMove[i]=="BL'" or lstMove[i]=="BL2" or lstMove[i]=="BL2'" or lstMove[i]=="BL3" or lstMove[i]=="BL3'"):
                if(lstMove[i]=="BL"):
                    self = self.move_BL()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BL'"):
                    self = self.move_BL_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BL2"):
                    self = self.move_BL2()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BL3"):
                    self = self.move_BL3()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BL2'"):
                    self = self.move_BL2_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BL3'"):
                    self = self.move_BL3_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
            if(lstMove[i]=="BR" or lstMove[i]=="BR'" or lstMove[i]=="BR2" or lstMove[i]=="BR2'" or lstMove[i]=="BR3" or lstMove[i]=="BR3'"):
                if(lstMove[i]=="BR"):
                    self = self.move_BR()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BR'"):
                    self = self.move_BR_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BR2"):
                    self = self.move_BR2()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BR3"):
                    self = self.move_BR3()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BR2'"):
                    self = self.move_BR2_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
                elif(lstMove[i]=="BR3'"):
                    self = self.move_BR3_prime()
                    self.drawMegaminx(scr)
                    Megaminx.sleeper(delay)
        return self
            
            
    def move_y(self):
        u = FaceUtils3.rotate(self.up)
        f = FaceUtils3.transfert(self.right)
        l = FaceUtils3.transfert(self.front)
        r = FaceUtils3.transfert(self.backRight)
        bl = FaceUtils3.transfert(self.left)
        br = FaceUtils3.transfert(self.backLeft)
        d = FaceUtils3.rotateAsync(self.down)
        dl = FaceUtils3.transfert(self.downRight)
        dr = FaceUtils3.transfert(self.absRight)
        al = FaceUtils3.transfert(self.downLeft)
        ar = FaceUtils3.transfert(self.back)
        b = FaceUtils3.transfert(self.absLeft)
        
        return Megaminx(
            full="no", 
            up=u, front=f, left=l, right=r, 
            backLeft=bl, backRight=br,
            down=d, downLeft=dl, downRight=dr,
            absLeft=al, absRight=ar, back=b)
    
    def move_y_prime(self):
        u = FaceUtils3.rotateAsync(self.up)
        f = FaceUtils3.transfert(self.left)
        l = FaceUtils3.transfert(self.backLeft)
        r = FaceUtils3.transfert(self.front)
        bl = FaceUtils3.transfert(self.backRight)
        br = FaceUtils3.transfert(self.right)
        d = FaceUtils3.rotate(self.down)
        dl = FaceUtils3.transfert(self.absLeft)
        dr = FaceUtils3.transfert(self.downLeft)
        al = FaceUtils3.transfert(self.back)
        ar = FaceUtils3.transfert(self.downRight)
        b = FaceUtils3.transfert(self.absRight)
        
        return Megaminx(
            full="no", 
            up=u, front=f, left=l, right=r, 
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar,back=b)
        
    def move_y2(self):
        m = self.move_y()
        return m.move_y()
    
    def move_y2_prime(self):
        m = self.move_y_prime()
        return m.move_y_prime()
    
    def move_y3(self):
        m = self.move_y2()
        return m.move_y()
    
    def move_y3_prime(self):
        m = self.move_y2_prime()
        return m.move_y_prime()

    def move_z(self):
        u = FaceUtils3.rotate(self.left)
        f = FaceUtils3.rotate(self.front)
        l = FaceUtils3.rotate(self.downLeft)
        r = FaceUtils3.rotateTwice(self.up)
        bl = FaceUtils3.transfert(self.absLeft)
        br = FaceUtils3.rotateAsync(self.backLeft)
        d = FaceUtils3.rotate(self.absRight)
        dl = FaceUtils3.rotate(self.downRight)
        dr = FaceUtils3.transfert(self.right)
        al = FaceUtils3.rotate(self.down)
        ar = FaceUtils3.rotateAsync(self.backRight)
        b = FaceUtils3.rotateAsync(self.back)

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_z_prime(self):
        u = FaceUtils3.rotateTwiceAsync(self.right)
        f = FaceUtils3.rotateAsync(self.front)
        l =  FaceUtils3.rotateAsync(self.up)
        r = FaceUtils3.transfert(self.downRight)
        bl = FaceUtils3.rotate(self.backRight)
        br = FaceUtils3.rotate(self.absRight)
        d = FaceUtils3.rotateAsync(self.absLeft)
        dl = FaceUtils3.rotateAsync(self.left)
        dr = FaceUtils3.rotateAsync(self.downLeft)
        al = FaceUtils3.transfert(self.backLeft)
        ar = FaceUtils3.rotateAsync(self.down)
        b = FaceUtils3.rotate(self.back)

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_z2(self):
        m = self.move_z()
        return m.move_z()

    def move_z2_prime(self):
        m = self.move_z_prime()
        return m.move_z_prime()

    def move_z3(self):
        m = self.move_z2()
        return m.move_z()

    def move_z3_prime(self):
        m = self.move_z2_prime()
        return m.move_y_prime()

    def move_U(self):
        u = FaceUtils3.rotate(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        for i in range(3):
            f[i] = self.right[i]
        for i in range(3):
            l[i] = self.front[i]
        for i in range(3):
            r[i] = self.backRight[i]
        for i in range(3):
            bl[i] = self.left[i]
        for i in range(3):
            br[i] = self.backLeft[i]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_U_prime(self):
        u = FaceUtils3.rotateAsync(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        for i in range(3):
            f[i] = self.left[i]
        for i in range(3):
            l[i] = self.backLeft[i]
        for i in range(3):
            r[i] = self.front[i]
        for i in range(3):
            bl[i] = self.backRight[i]
        for i in range(3):
            br[i] = self.right[i]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_U2(self):
        m = self.move_U()
        return m.move_U()

    def move_U3(self):
        m = self.move_U2()
        return m.move_U()

    def move_U2_prime(self):
        m = self.move_U_prime()
        return m.move_U_prime()

    def move_U3_prime(self):
        m = self.move_U2_prime()
        return m.move_U_prime()   

    def move_R(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.rotate(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        for i in range(2,5,1):
            u[i] = self.front[i]
        
        f[2], f[3], f[4] = self.downRight[0], self.downRight[1], self.downRight[2]
        dr[0], dr[1], dr[2] = self.absRight[8], self.absRight[9], self.absRight[0]
        ar[8], ar[9], ar[0] = self.backRight[8], self.backRight[9], self.backRight[0]
        br[8], br[9], br[0] = self.up[2], self.up[3], self.up[4]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_R_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.rotateAsync(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[2], u[3], u[4] = self.backRight[8], self.backRight[9], self.backRight[0]
        f[2], f[3], f[4] = self.up[2], self.up[3], self.up[4]
        dr[0], dr[1], dr[2] = self.front[2], self.front[3], self.front[4]
        ar[8], ar[9], ar[0] = self.downRight[0], self.downRight[1], self.downRight[2]
        br[8], br[9], br[0] = self.absRight[8], self.absRight[9], self.absRight[0]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    
    def move_R2(self):
        m = self.move_R()
        return m.move_R()

    def move_R3(self):
        m = self.move_R2()
        return m.move_R()

    def move_R2_prime(self):
        m = self.move_R_prime()
        return m.move_R_prime()

    def move_R3_prime(self):
        m = self.move_R2_prime()
        return m.move_R_prime()

    def move_L(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.rotate(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[8], u[7], u[6] = self.backLeft[4], self.backLeft[3], self.backLeft[2]
        f[0], f[9], f[8] = self.up[8], self.up[7], self.up[6]
        dl[0], dl[9], dl[8] = self.front[0], self.front[9], self.front[8]
        al[0], al[1], al[2] = self.downLeft[8], self.downLeft[9], self.downLeft[0]
        bl[2], bl[3], bl[4] = self.absLeft[0], self.absLeft[1], self.absLeft[2]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_L_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.rotateAsync(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[8], u[7], u[6] = self.front[0], self.front[9], self.front[8]
        f[0], f[9], f[8] = self.downLeft[0], self.downLeft[9], self.downLeft[8]
        dl[0], dl[9], dl[8] = self.absLeft[2], self.absLeft[1], self.absLeft[0]
        al[0], al[1], al[2] = self.backLeft[2], self.backLeft[3], self.backLeft[4]
        bl[2], bl[3], bl[4] = self.up[6], self.up[7], self.up[8]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )
    
    def move_L2(self):
        m = self.move_L()
        return m.move_L()

    def move_L3(self):
        m = self.move_L2()
        return m.move_L()

    def move_L2_prime(self):
        m = self.move_L_prime()
        return m.move_L_prime()

    def move_L3_prime(self):
        m = self.move_L2_prime()
        return m.move_L_prime()
    
    def move_F(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.rotate(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[6], u[5], u[4] = self.left[4], self.left[3], self.left[2]
        r[0], r[9], r[8] = self.up[6], self.up[5], self.up[4]
        dr[0], dr[9], dr[8] = self.right[0], self.right[9], self.right[8]
        dl[0], dl[1], dl[2] = self.downRight[8], self.downRight[9], self.downRight[0]
        l[2], l[3], l[4] = self.downLeft[0], self.downLeft[1], self.downLeft[2]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_F_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.rotateAsync(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[6], u[5], u[4] = self.right[0], self.right[9], self.right[8]
        r[0], r[9], r[8] = self.downRight[0], self.downRight[9], self.downRight[8]
        dr[0], dr[9], dr[8] = self.downLeft[2], self.downLeft[1], self.downLeft[0]
        dl[0], dl[1], dl[2] = self.left[2], self.left[3], self.left[4]
        l[2], l[3], l[4] = self.up[4], self.up[5], self.up[6]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )
    
    def move_F2(self):
        m = self.move_F()
        return m.move_F()

    def move_F3(self):
        m = self.move_F2()
        return m.move_F()

    def move_F2_prime(self):
        m = self.move_F_prime()
        return m.move_F_prime()

    def move_F3_prime(self):
        m = self.move_F2_prime()
        return m.move_F_prime()

    def move_DL(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.rotate(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        l[4], l[5], l[6] = self.absLeft[2], self.absLeft[3], self.absLeft[4]
        f[6], f[7], f[8] = self.left[4], self.left[5], self.left[6]
        dr[6], dr[7], dr[8] = self.front[6], self.front[7], self.front[8]
        d[0], d[9], d[8] = self.downRight[8], self.downRight[7], self.downRight[6]
        al[2], al[3], al[4] = self.down[8], self.down[9], self.down[0]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_DL_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.rotateAsync(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        l[4], l[5], l[6] = self.front[6], self.front[7], self.front[8]
        f[6], f[7], f[8] = self.downRight[6], self.downRight[7], self.downRight[8]
        dr[6], dr[7], dr[8] = self.down[8], self.down[9], self.down[0]
        d[0], d[9], d[8] = self.absLeft[4], self.absLeft[3], self.absLeft[2]
        al[2], al[3], al[4] = self.left[4], self.left[5], self.left[6]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_DL2(self):
        m = self.move_DL()
        return m.move_DL()

    def move_DL3(self):
        m = self.move_DL2()
        return m.move_DL()

    def move_DL2_prime(self):
        m = self.move_DL_prime()
        return m.move_DL_prime()

    def move_DL3_prime(self):
        m = self.move_DL2_prime()
        return m.move_DL_prime()
    
    def move_DR(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.rotate(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        f[4], f[5], f[6] = self.downLeft[2], self.downLeft[3], self.downLeft[4]
        r[6], r[7], r[8] = self.front[4], self.front[5], self.front[6]
        dl[2], dl[3], dl[4] = self.down[0], self.down[1], self.down[2]
        ar[6], ar[7], ar[8] = self.right[6], self.right[7], self.right[8]
        d[0], d[1], d[2] = self.absRight[6], self.absRight[7], self.absRight[8]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_DR_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.rotateAsync(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        f[4], f[5], f[6] = self.right[6], self.right[7], self.right[8]
        r[6], r[7], r[8] = self.absRight[6], self.absRight[7], self.absRight[8]
        dl[2], dl[3], dl[4] = self.front[4], self.front[5], self.front[6]
        ar[6], ar[7], ar[8] = self.down[0], self.down[1], self.down[2]
        d[0], d[1], d[2] = self.downLeft[2], self.downLeft[3], self.downLeft[4]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_DR2(self):
        m = self.move_DR()
        return m.move_DR()

    def move_DR3(self):
        m = self.move_DR2()
        return m.move_DR()

    def move_DR2_prime(self):
        m = self.move_DR_prime()
        return m.move_DR_prime()

    def move_DR3_prime(self):
        m = self.move_DR2_prime()
        return m.move_DR_prime()
    
    def move_D(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.rotate(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        dl[4], dl[5], dl[6] = self.absLeft[4], self.absLeft[5], self.absLeft[6]
        dr[4], dr[5], dr[6] = self.downLeft[4], self.downLeft[5], self.downLeft[6]
        ar[4], ar[5], ar[6] = self.downRight[4], self.downRight[5], self.downRight[6]
        al[4], al[5], al[6] = self.back[4], self.back[5], self.back[6]
        b[4], b[5], b[6] = self.absRight[4], self.absRight[5], self.absRight[6]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )
    
    def move_D_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.rotateAsync(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        dl[4], dl[5], dl[6] = self.downRight[4], self.downRight[5], self.downRight[6]
        dr[4], dr[5], dr[6] = self.absRight[4], self.absRight[5], self.absRight[6]
        ar[4], ar[5], ar[6] = self.back[4], self.back[5], self.back[6]
        al[4], al[5], al[6] = self.downLeft[4], self.downLeft[5], self.downLeft[6]
        b[4], b[5], b[6] = self.absLeft[4], self.absLeft[5], self.absLeft[6]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )
    
    def move_D2(self):
        m = self.move_D()
        return m.move_D()

    def move_D3(self):
        m = self.move_D2()
        return m.move_D()

    def move_D2_prime(self):
        m = self.move_D_prime()
        return m.move_D_prime()

    def move_D3_prime(self):
        m = self.move_D2_prime()
        return m.move_D_prime()

    def move_BL(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.rotate(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[8], u[9], u[0] = self.backRight[2], self.backRight[3], self.backRight[4]
        l[8], l[9], l[0] = self.up[8], self.up[9], self.up[0]
        br[2], br[3], br[4] = self.back[0], self.back[1], self.back[2]
        b[0], b[1], b[2] = self.absLeft[8], self.absLeft[9], self.absLeft[0]
        al[8], al[9], al[0] = self.left[8], self.left[9], self.left[0]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )
    
    def move_BL_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.rotateAsync(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[8], u[9], u[0] = self.left[8], self.left[9], self.left[0]
        l[8], l[9], l[0] = self.absLeft[8], self.absLeft[9], self.absLeft[0]
        br[2], br[3], br[4] = self.up[8], self.up[9], self.up[0]
        b[0], b[1], b[2] = self.backRight[2], self.backRight[3], self.backRight[4]
        al[8], al[9], al[0] = self.back[0], self.back[1], self.back[2]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_BL2(self):
        m = self.move_BL()
        return m.move_BL()

    def move_BL3(self):
        m = self.move_BL2()
        return m.move_BL()

    def move_BL2_prime(self):
        m = self.move_BL_prime()
        return m.move_BL_prime()

    def move_BL3_prime(self):
        m = self.move_BL2_prime()
        return m.move_BL_prime()
    
    def move_BR(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.rotate(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[0], u[1], u[2] = self.right[2], self.right[3], self.right[4]
        r[2], r[3], r[4] = self.absRight[0], self.absRight[1], self.absRight[2]
        bl[8], bl[9], bl[0] = self.up[0], self.up[1], self.up[2]
        b[8], b[9], b[0] = self.backLeft[8], self.backLeft[9], self.backLeft[0]
        ar[0], ar[1], ar[2] = self.back[8], self.back[9], self.back[0]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )
    
    def move_BR_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.rotateAsync(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[0], u[1], u[2] = self.backLeft[8], self.backLeft[9], self.backLeft[0]
        r[2], r[3], r[4] = self.up[0], self.up[1], self.up[2]
        bl[8], bl[9], bl[0] = self.back[8], self.back[9], self.back[0]
        b[8], b[9], b[0] = self.absRight[0], self.absRight[1], self.absRight[2]
        ar[0], ar[1], ar[2] = self.right[2], self.right[3], self.right[4]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_BR2(self):
        m = self.move_BR()
        return m.move_BR()

    def move_BR3(self):
        m = self.move_BR2()
        return m.move_BR()

    def move_BR2_prime(self):
        m = self.move_BR_prime()
        return m.move_BR_prime()

    def move_BR3_prime(self):
        m = self.move_BR2_prime()
        return m.move_BR_prime()

    def move_AL(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.rotate(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        dl[6], dl[7], dl[8] = self.left[6], self.left[7], self.left[8]
        l[6], l[7], l[8] = self.backLeft[4], self.backLeft[5], self.backLeft[6]
        d[6], d[7], d[8] = self.downLeft[6], self.downLeft[7], self.downLeft[8]
        bl[4], bl[5], bl[6] = self.back[2], self.back[3], self.back[4]
        b[2], b[3], b[4] = self.down[6], self.down[7], self.down[8]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_AL_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.rotateAsync(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        dl[6], dl[7], dl[8] = self.down[6], self.down[7], self.down[8]
        l[6], l[7], l[8] = self.downLeft[6], self.downLeft[7], self.downLeft[8]
        d[6], d[7], d[8] = self.back[2], self.back[3], self.back[4]
        bl[4], bl[5], bl[6] = self.left[6], self.left[7], self.left[8]
        b[2], b[3], b[4] = self.backLeft[4], self.backLeft[5], self.backLeft[6]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )
    
    def move_AL2(self):
        m = self.move_AL()
        return m.move_AL()

    def move_AL3(self):
        m = self.move_AL2()
        return m.move_AL()

    def move_AL2_prime(self):
        m = self.move_AL_prime()
        return m.move_AL_prime()

    def move_AL3_prime(self):
        m = self.move_AL2_prime()
        return m.move_AL_prime()
    
    def move_AR(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.rotate(self.absRight)
        b = FaceUtils3.transfert(self.back)

        dr[2], dr[3], dr[4] = self.down[2], self.down[3], self.down[4]
        r[4], r[5], r[6] = self.downRight[2], self.downRight[3], self.downRight[4]
        br[6], br[7], br[8] = self.right[4], self.right[5], self.right[6]
        d[2], d[3], d[4] = self.back[6], self.back[7], self.back[8]
        b[6], b[7], b[8] = self.backRight[6], self.backRight[7], self.backRight[8]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_AR_prime(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.rotateAsync(self.absRight)
        b = FaceUtils3.transfert(self.back)

        dr[2], dr[3], dr[4] = self.right[4], self.right[5], self.right[6]
        r[4], r[5], r[6] = self.backRight[6], self.backRight[7], self.backRight[8]
        br[6], br[7], br[8] = self.back[6], self.back[7], self.back[8]
        d[2], d[3], d[4] = self.downRight[2], self.downRight[3], self.downRight[4]
        b[6], b[7], b[8] = self.down[2], self.down[3], self.down[4]

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )
    
    def move_AR2(self):
        m = self.move_AR()
        return m.move_AR()

    def move_AR3(self):
        m = self.move_AR2()
        return m.move_AR()

    def move_AR2_prime(self):
        m = self.move_AR_prime()
        return m.move_AR_prime()

    def move_AR3_prime(self):
        m = self.move_AR2_prime()
        return m.move_AR_prime()


    def move_RPP(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[9], u[0], u[1], u[2], u[3], u[4], u[5], u[10] = self.downLeft[1], self.downLeft[2], self.downLeft[3], self.downLeft[4], self.downLeft[5], self.downLeft[6], self.downLeft[7], self.downLeft[10]
        f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[10] = self.absLeft[3], self.absLeft[4], self.absLeft[5], self.absLeft[6], self.absLeft[7], self.absLeft[8], self.absLeft[9], self.absLeft[10]
        r = FaceUtils3.rotate(self.down)
        bl[5], bl[6], bl[7], bl[8], bl[9], bl[0], bl[1], bl[10] = self.front[1], self.front[2], self.front[3], self.front[4], self.front[5], self.front[6], self.front[7], self.front[10]
        br = FaceUtils3.rotateTwice(self.downRight)
        d = FaceUtils3.rotateTwiceAsync(self.backRight)
        dl[1], dl[2], dl[3], dl[4], dl[5], dl[6], dl[7], dl[10] = self.backLeft[5], self.backLeft[6], self.backLeft[7], self.backLeft[8], self.backLeft[9], self.backLeft[0], self.backLeft[1], self.backLeft[10]
        dr = FaceUtils3.rotateTwiceAsync(self.back)
        al[3], al[4], al[5], al[6], al[7], al[8], al[9], al[10] = self.up[9], self.up[0], self.up[1], self.up[2], self.up[3], self.up[4], self.up[5], self.up[10]
        ar = FaceUtils3.rotateTwice(self.absRight)
        b = FaceUtils3.rotate(self.right)

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )
    
    def move_RMM(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        u[9], u[0], u[1], u[2], u[3], u[4], u[5], u[10] = self.absLeft[3], self.absLeft[4], self.absLeft[5], self.absLeft[6], self.absLeft[7], self.absLeft[8], self.absLeft[9], self.absLeft[10]
        f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[10] = self.backLeft[5], self.backLeft[6], self.backLeft[7], self.backLeft[8], self.backLeft[9], self.backLeft[0], self.backLeft[1], self.backLeft[10]
        r = FaceUtils3.rotateAsync(self.back)
        bl[5], bl[6], bl[7], bl[8], bl[9], bl[0], bl[1], bl[10] = self.downLeft[1], self.downLeft[2], self.downLeft[3], self.downLeft[4], self.downLeft[5], self.downLeft[6], self.downLeft[7], self.downLeft[10]
        br = FaceUtils3.rotateTwice(self.down)
        d = FaceUtils3.rotateAsync(self.right)
        dl[1], dl[2], dl[3], dl[4], dl[5], dl[6], dl[7], dl[10] = self.up[9], self.up[0], self.up[1], self.up[2], self.up[3], self.up[4], self.up[5], self.up[10]
        dr = FaceUtils3.rotateTwiceAsync(self.backRight)
        al[3], al[4], al[5], al[6], al[7], al[8], al[9], al[10] = self.front[1], self.front[2], self.front[3], self.front[4], self.front[5], self.front[6], self.front[7], self.front[10]
        ar = FaceUtils3.rotateTwiceAsync(self.absRight)
        b = FaceUtils3.rotateTwice(self.downRight)

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_DPP(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        for i in range(3,11,1):
            f[i] = self.backLeft[i]
        for i in range(3,11,1):
            l[i] = self.backRight[i]
        for i in range(3,11,1):
            r[i] = self.left[i]
        for i in range(3,11,1):
            bl[i] = self.right[i]
        for i in range(3,11,1):
            br[i] = self.front[i]
        
        d = FaceUtils3.rotateTwice(self.down)
        dl = FaceUtils3.transfert(self.back)
        dr = FaceUtils3.transfert(self.absLeft)
        al = FaceUtils3.transfert(self.absRight)
        ar = FaceUtils3.transfert(self.downLeft)
        b = FaceUtils3.transfert(self.downRight)

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )

    def move_DMM(self):
        u = FaceUtils3.transfert(self.up)
        f = FaceUtils3.transfert(self.front)
        l = FaceUtils3.transfert(self.left)
        r = FaceUtils3.transfert(self.right)
        bl = FaceUtils3.transfert(self.backLeft)
        br = FaceUtils3.transfert(self.backRight)
        d = FaceUtils3.transfert(self.down)
        dl = FaceUtils3.transfert(self.downLeft)
        dr = FaceUtils3.transfert(self.downRight)
        al = FaceUtils3.transfert(self.absLeft)
        ar = FaceUtils3.transfert(self.absRight)
        b = FaceUtils3.transfert(self.back)

        for i in range(3,11,1):
            f[i] = self.backRight[i]
        for i in range(3,11,1):
            l[i] = self.right[i]
        for i in range(3,11,1):
            r[i] = self.backLeft[i]
        for i in range(3,11,1):
            bl[i] = self.front[i]
        for i in range(3,11,1):
            br[i] = self.left[i]
        
        d = FaceUtils3.rotateTwiceAsync(self.down)
        dl = FaceUtils3.transfert(self.absRight)
        dr = FaceUtils3.transfert(self.back)
        al = FaceUtils3.transfert(self.downRight)
        ar = FaceUtils3.transfert(self.absLeft)
        b = FaceUtils3.transfert(self.downLeft)

        return Megaminx(
            full="no",
            up=u,front=f,left=l,right=r,
            backLeft=bl,backRight=br,
            down=d,downLeft=dl,downRight=dr,
            absLeft=al,absRight=ar, back=b
        )