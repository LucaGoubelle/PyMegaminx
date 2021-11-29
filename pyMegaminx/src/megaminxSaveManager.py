import json
import megaminx
from megaminx import Sticker

class SaveManager:
    def __init__(self):
        self.filePath = "../res/minx3.json"
        self.data = self.loadJson()
    
    def loadJson(self):
        with open(self.filePath) as file:
            data = json.load(file)
        return data

    def loadData(self):
        u = [None for i in range(11)]
        l = [None for i in range(11)]
        r = [None for i in range(11)]
        f = [None for i in range(11)]
        bl = [None for i in range(11)]
        br = [None for i in range(11)]
        b = [None for i in range(11)]
        d = [None for i in range(11)]
        dl = [None for i in range(11)]
        dr = [None for i in range(11)]
        al = [None for i in range(11)]
        ar = [None for i in range(11)]

        """for i in range(11): u.append(None)
        for i in range(11): l.append(None)
        for i in range(11): r.append(None)
        for i in range(11): f.append(None)
        for i in range(11): bl.append(None)

        for i in range(11): br.append(None)
        for i in range(11): b.append(None)
        for i in range(11): d.append(None)
        for i in range(11): dl.append(None)
        for i in range(11): dr.append(None)

        for i in range(11): al.append(None)
        for i in range(11): ar.append(None)"""

        for i in range(len(self.data["up"])):
            if self.data["up"][i] == "white": u[i] = Sticker("white")
            elif self.data["up"][i] == "blue": u[i] = Sticker("blue")
            elif self.data["up"][i] == "red": u[i] = Sticker("red")
            elif self.data["up"][i] == "yellow": u[i] = Sticker("yellow")
            elif self.data["up"][i] == "green": u[i] = Sticker("green")

            elif self.data["up"][i] == "purple": u[i] = Sticker("purple")
            elif self.data["up"][i] == "pink": u[i] = Sticker("pink")
            elif self.data["up"][i] == "lime": u[i] = Sticker("lime")
            elif self.data["up"][i] == "orange": u[i] = Sticker("orange")
            elif self.data["up"][i] == "cyan": u[i] = Sticker("cyan")

            elif self.data["up"][i] == "beige": u[i] = Sticker("beige")
            elif self.data["up"][i] == "grey": u[i] = Sticker("grey")
        
        for i in range(len(self.data["left"])):
            if self.data["left"][i] == "white": l[i] = Sticker("white")
            elif self.data["left"][i] == "blue": l[i] = Sticker("blue")
            elif self.data["left"][i] == "red": l[i] = Sticker("red")
            elif self.data["left"][i] == "yellow": l[i] = Sticker("yellow")
            elif self.data["left"][i] == "green": l[i] = Sticker("green")

            elif self.data["left"][i] == "purple": l[i] = Sticker("purple")
            elif self.data["left"][i] == "pink": l[i] = Sticker("pink")
            elif self.data["left"][i] == "lime": l[i] = Sticker("lime")
            elif self.data["left"][i] == "orange": l[i] = Sticker("orange")
            elif self.data["left"][i] == "cyan": l[i] = Sticker("cyan")

            elif self.data["left"][i] == "beige": l[i] = Sticker("beige")
            elif self.data["left"][i] == "grey": l[i] = Sticker("grey")

        for i in range(len(self.data["right"])):
            if self.data["right"][i] == "white": r[i] = Sticker("white")
            elif self.data["right"][i] == "blue": r[i] = Sticker("blue")
            elif self.data["right"][i] == "red": r[i] = Sticker("red")
            elif self.data["right"][i] == "yellow": r[i] = Sticker("yellow")
            elif self.data["right"][i] == "green": r[i] = Sticker("green")

            elif self.data["right"][i] == "purple": r[i] = Sticker("purple")
            elif self.data["right"][i] == "pink": r[i] = Sticker("pink")
            elif self.data["right"][i] == "lime": r[i] = Sticker("lime")
            elif self.data["right"][i] == "orange": r[i] = Sticker("orange")
            elif self.data["right"][i] == "cyan": r[i] = Sticker("cyan")

            elif self.data["right"][i] == "beige": r[i] = Sticker("beige")
            elif self.data["right"][i] == "grey": r[i] = Sticker("grey")

        for i in range(len(self.data["front"])):
            if self.data["front"][i] == "white": f[i] = Sticker("white")
            elif self.data["front"][i] == "blue": f[i] = Sticker("blue")
            elif self.data["front"][i] == "red": f[i] = Sticker("red")
            elif self.data["front"][i] == "yellow": f[i] = Sticker("yellow")
            elif self.data["front"][i] == "green": f[i] = Sticker("green")

            elif self.data["front"][i] == "purple": f[i] = Sticker("purple")
            elif self.data["front"][i] == "pink": f[i] = Sticker("pink")
            elif self.data["front"][i] == "lime": f[i] = Sticker("lime")
            elif self.data["front"][i] == "orange": f[i] = Sticker("orange")
            elif self.data["front"][i] == "cyan": f[i] = Sticker("cyan")

            elif self.data["front"][i] == "beige": f[i] = Sticker("beige")
            elif self.data["front"][i] == "grey": f[i] = Sticker("grey")
        
        for i in range(len(self.data["backLeft"])):
            if self.data["backLeft"][i] == "white": bl[i] = Sticker("white")
            elif self.data["backLeft"][i] == "blue": bl[i] = Sticker("blue")
            elif self.data["backLeft"][i] == "red": bl[i] = Sticker("red")
            elif self.data["backLeft"][i] == "yellow": bl[i] = Sticker("yellow")
            elif self.data["backLeft"][i] == "green": bl[i] = Sticker("green")

            elif self.data["backLeft"][i] == "purple": bl[i] = Sticker("purple")
            elif self.data["backLeft"][i] == "pink": bl[i] = Sticker("pink")
            elif self.data["backLeft"][i] == "lime": bl[i] = Sticker("lime")
            elif self.data["backLeft"][i] == "orange": bl[i] = Sticker("orange")
            elif self.data["backLeft"][i] == "cyan": bl[i] = Sticker("cyan")

            elif self.data["backLeft"][i] == "beige": bl[i] = Sticker("beige")
            elif self.data["backLeft"][i] == "grey": bl[i] = Sticker("grey")
        
        for i in range(len(self.data["backRight"])):
            if self.data["backRight"][i] == "white": br[i] = Sticker("white")
            elif self.data["backRight"][i] == "blue": br[i] = Sticker("blue")
            elif self.data["backRight"][i] == "red": br[i] = Sticker("red")
            elif self.data["backRight"][i] == "yellow": br[i] = Sticker("yellow")
            elif self.data["backRight"][i] == "green": br[i] = Sticker("green")

            elif self.data["backRight"][i] == "purple": br[i] = Sticker("purple")
            elif self.data["backRight"][i] == "pink": br[i] = Sticker("pink")
            elif self.data["backRight"][i] == "lime": br[i] = Sticker("lime")
            elif self.data["backRight"][i] == "orange": br[i] = Sticker("orange")
            elif self.data["backRight"][i] == "cyan": br[i] = Sticker("cyan")

            elif self.data["backRight"][i] == "beige": br[i] = Sticker("beige")
            elif self.data["backRight"][i] == "grey": br[i] = Sticker("grey")
        
        for i in range(len(self.data["back"])):
            if self.data["back"][i] == "white": b[i] = Sticker("white")
            elif self.data["back"][i] == "blue": b[i] = Sticker("blue")
            elif self.data["back"][i] == "red": b[i] = Sticker("red")
            elif self.data["back"][i] == "yellow": b[i] = Sticker("yellow")
            elif self.data["back"][i] == "green": b[i] = Sticker("green")

            elif self.data["back"][i] == "purple": b[i] = Sticker("purple")
            elif self.data["back"][i] == "pink": b[i] = Sticker("pink")
            elif self.data["back"][i] == "lime": b[i] = Sticker("lime")
            elif self.data["back"][i] == "orange": b[i] = Sticker("orange")
            elif self.data["back"][i] == "cyan": b[i] = Sticker("cyan")

            elif self.data["back"][i] == "beige": b[i] = Sticker("beige")
            elif self.data["back"][i] == "grey": b[i] = Sticker("grey")

        for i in range(len(self.data["downLeft"])):
            if self.data["downLeft"][i] == "white": dl[i] = Sticker("white")
            elif self.data["downLeft"][i] == "blue": dl[i] = Sticker("blue")
            elif self.data["downLeft"][i] == "red": dl[i] = Sticker("red")
            elif self.data["downLeft"][i] == "yellow": dl[i] = Sticker("yellow")
            elif self.data["downLeft"][i] == "green": dl[i] = Sticker("green")

            elif self.data["downLeft"][i] == "purple": dl[i] = Sticker("purple")
            elif self.data["downLeft"][i] == "pink": dl[i] = Sticker("pink")
            elif self.data["downLeft"][i] == "lime": dl[i] = Sticker("lime")
            elif self.data["downLeft"][i] == "orange": dl[i] = Sticker("orange")
            elif self.data["downLeft"][i] == "cyan": dl[i] = Sticker("cyan")

            elif self.data["downLeft"][i] == "beige": dl[i] = Sticker("beige")
            elif self.data["downLeft"][i] == "grey": dl[i] = Sticker("grey")

        for i in range(len(self.data["downRight"])):
            if self.data["downRight"][i] == "white": dr[i] = Sticker("white")
            elif self.data["downRight"][i] == "blue": dr[i] = Sticker("blue")
            elif self.data["downRight"][i] == "red": dr[i] = Sticker("red")
            elif self.data["downRight"][i] == "yellow": dr[i] = Sticker("yellow")
            elif self.data["downRight"][i] == "green": dr[i] = Sticker("green")

            elif self.data["downRight"][i] == "purple": dr[i] = Sticker("purple")
            elif self.data["downRight"][i] == "pink": dr[i] = Sticker("pink")
            elif self.data["downRight"][i] == "lime": dr[i] = Sticker("lime")
            elif self.data["downRight"][i] == "orange": dr[i] = Sticker("orange")
            elif self.data["downRight"][i] == "cyan": dr[i] = Sticker("cyan")

            elif self.data["downRight"][i] == "beige": dr[i] = Sticker("beige")
            elif self.data["downRight"][i] == "grey": dr[i] = Sticker("grey")
        
        for i in range(len(self.data["down"])):
            if self.data["down"][i] == "white": d[i] = Sticker("white")
            elif self.data["down"][i] == "blue": d[i] = Sticker("blue")
            elif self.data["down"][i] == "red": d[i] = Sticker("red")
            elif self.data["down"][i] == "yellow": d[i] = Sticker("yellow")
            elif self.data["down"][i] == "green": d[i] = Sticker("green")

            elif self.data["down"][i] == "purple": d[i] = Sticker("purple")
            elif self.data["down"][i] == "pink": d[i] = Sticker("pink")
            elif self.data["down"][i] == "lime": d[i] = Sticker("lime")
            elif self.data["down"][i] == "orange": d[i] = Sticker("orange")
            elif self.data["down"][i] == "cyan": d[i] = Sticker("cyan")

            elif self.data["down"][i] == "beige": d[i] = Sticker("beige")
            elif self.data["down"][i] == "grey": d[i] = Sticker("grey")

        for i in range(len(self.data["absLeft"])):
            if self.data["absLeft"][i] == "white": al[i] = Sticker("white")
            elif self.data["absLeft"][i] == "blue": al[i] = Sticker("blue")
            elif self.data["absLeft"][i] == "red": al[i] = Sticker("red")
            elif self.data["absLeft"][i] == "yellow": al[i] = Sticker("yellow")
            elif self.data["absLeft"][i] == "green": al[i] = Sticker("green")

            elif self.data["absLeft"][i] == "purple": al[i] = Sticker("purple")
            elif self.data["absLeft"][i] == "pink": al[i] = Sticker("pink")
            elif self.data["absLeft"][i] == "lime": al[i] = Sticker("lime")
            elif self.data["absLeft"][i] == "orange": al[i] = Sticker("orange")
            elif self.data["absLeft"][i] == "cyan": al[i] = Sticker("cyan")

            elif self.data["absLeft"][i] == "beige": al[i] = Sticker("beige")
            elif self.data["absLeft"][i] == "grey": al[i] = Sticker("grey")

        for i in range(len(self.data["absRight"])):
            if self.data["absRight"][i] == "white": ar[i] = Sticker("white")
            elif self.data["absRight"][i] == "blue": ar[i] = Sticker("blue")
            elif self.data["absRight"][i] == "red": ar[i] = Sticker("red")
            elif self.data["absRight"][i] == "yellow": ar[i] = Sticker("yellow")
            elif self.data["absRight"][i] == "green": ar[i] = Sticker("green")

            elif self.data["absRight"][i] == "purple": ar[i] = Sticker("purple")
            elif self.data["absRight"][i] == "pink": ar[i] = Sticker("pink")
            elif self.data["absRight"][i] == "lime": ar[i] = Sticker("lime")
            elif self.data["absRight"][i] == "orange": ar[i] = Sticker("orange")
            elif self.data["absRight"][i] == "cyan": ar[i] = Sticker("cyan")

            elif self.data["absRight"][i] == "beige": ar[i] = Sticker("beige")
            elif self.data["absRight"][i] == "grey": ar[i] = Sticker("grey")

        return megaminx.Megaminx(
            full="no",
            up=u, left=l, right=r, front=f,
            backLeft=bl, backRight=br, back=b,
            downLeft=dl, downRight=dr, down=d,
            absLeft=al, absRight=ar
        )


    def saveData(self, minx):
        jdata = {
            "up": [None for i in range(11)],
            "front": [None for i in range(11)],
            "left": [None for i in range(11)],
            "right": [None for i in range(11)],
            "backLeft": [None for i in range(11)],

            "backRight": [None for i in range(11)],
            "back": [None for i in range(11)],
            "downLeft": [None for i in range(11)],
            "downRight": [None for i in range(11)],
            "down": [None for i in range(11)],

            "absLeft": [None for i in range(11)],
            "absRight": [None for i in range(11)]
        }

        for k,v in jdata.items():
            if k == "up":
                for i in range(len(v)):
                    v[i] = minx.up[i].color
            elif k == "left":
                for i in range(len(v)):
                    v[i] = minx.left[i].color
            elif k == "front":
                for i in range(len(v)):
                    v[i] = minx.front[i].color
            elif k == "right":
                for i in range(len(v)):
                    v[i] = minx.right[i].color
            elif k == "backLeft":
                for i in range(len(v)):
                    v[i] = minx.backLeft[i].color
            elif k == "backRight":
                for i in range(len(v)):
                    v[i] = minx.backRight[i].color
            elif k == "back":
                for i in range(len(v)):
                    v[i] = minx.back[i].color
            elif k == "down":
                for i in range(len(v)):
                    v[i] = minx.down[i].color
            elif k == "downLeft":
                for i in range(len(v)):
                    v[i] = minx.downLeft[i].color
            elif k == "downRight":
                for i in range(len(v)):
                    v[i] = minx.downRight[i].color
            elif k == "absLeft":
                for i in range(len(v)):
                    v[i] = minx.absLeft[i].color
            elif k == "absRight":
                for i in range(len(v)):
                    v[i] = minx.absRight[i].color
        
        with open(self.filePath, "w") as file_object:
            json.dump(jdata, file_object, indent=4)