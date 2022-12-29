"""
    数据增强
"""
import os
import Augmentor
# path = "./ori"
# num = len(os.listdir("./mask"))
p = Augmentor.Pipeline("./ori")
p.ground_truth("./mask")
p.rotate180(probability=1)
p.sample(100)

#
# import os
# import Augmentor
# path = "/home/xhh/Desktop/Augmentor/ori"
#
# for name in os.listdir(path):
#     oldname = os.path.join(path, name)
#     newname = oldname.split(".")[0] + ".png"
#     os.renames(oldname, newname)

