################# GENERATING STRING #################

a = "/challenge/web-serveur/ch31/index.php" # String need to be generated

result = "concat("
for i in range (len(a)):
    if i != len(a) - 1:
        result += "char(" + str(ord(a[i])) + ") , "
    else:
        result += "char(" + str(ord(a[i])) + ") )"
print(result)
