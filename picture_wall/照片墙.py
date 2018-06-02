# 照片墙
# 520图案
"""
5：2，3，4,5,6,22,42,62,82,102,103,104,105,106,126,146,166,186,206,226,225,224,223,222
2：8,9,10,11,12,32,52,72,92,108,109,110,111,112,128,148,168,188,208,228,229,230,231,232
0：14,15,16，17,18,34,38,54,58,74,78,94,98,114,118,134,138,154,158,174,178,194,198,
214,218,234,235,236,237,238
"""
from PIL import Image
import os,sys

mw = 100  # 图片尺寸
ms = 20   # 单行图片数量

msize = mw*ms
toImage = Image.new('RGBA',(2000,2000))  # 合成图片像素点

# 像素点循环。一行一行将图片排列进去。
for y in range(1,21):
	for x in range(1,21):
		try:
			fromImage = Image.open(r"./%d.jpg" % (ms*(y-1)+x))			# 按图片编号逐张读取。
			fromImage = fromImage.resize((100,100),Image.ANTIALIAS)   # 100×100是每张旧图片的尺寸。
			toImage.paste(fromImage,((x-1)*mw,(y-1)*mw))		# 获取每个图片的坐标。然后逐张添加。
		except IOError:
			pass
toImage.show()

toImage.save('D:\\python学习班资料\\interesting\\照片墙\\family\\family.png')
