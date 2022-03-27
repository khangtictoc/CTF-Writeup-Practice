# ====================== MADE BY KHANGTICTOC ========================

a = "m3mbr35t4bl3" # String need to be generated

result = ""
for i in range (len(a)):
    if i != len(a) - 1:
        result += "chr(" + str(ord(a[i])) + ") || "
    else:
        result += "chr(" + str(ord(a[i])) + ")"
print(result)
