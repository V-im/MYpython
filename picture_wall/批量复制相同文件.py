import shutil
for i in range(1,401):
    shutil.copyfile("a.jpg","./%d.jpg" % i)
    i += 1



# with open("./a.jpg", "rb") as f:
#     content = f.read()
# for i in range(1,401):
#     with open("./%d.jpg" % i,"wb") as f1:
#         f1.write(content)
#         i += 1


