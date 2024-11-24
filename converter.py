indent =   "    "   #derzeitige einrückung
name = "keyboard."  #name der Tastatur und punkt
n = "\n"            #weil ich keine lust habe \ zu drücken
def duden(wort):
    match wort:
        case "todo":
            return 
        case _:
            print("duden hat nicht enthaltenes Wort erhalten: " + wort)
            return ""

crack_name = "test"

file_t_dir = "./Text/"+crack_name+"_T.txt"
file_c_dir = "./Code/"+crack_name+"_C.txt"

file_t = open(file_t_dir,"r")
txt = file_t.readlines()
file_t.close()

for i in range(len(txt)):
    txt[i] = txt[i].replace("\n", "")

file_c = open(file_c_dir,"w")
file_c.write("// Crackname: "+ txt[0] + "\n")
file_c.write("void " + txt[1] +  "() { \n")

for index in range(2,len(txt),2):
    print(txt[index])
    match txt[index]:
        case "text":
            file_c.write(indent+name+"print(\""+txt[index+1]+"\")"+n)
        case "textl":
            file_c.write(indent+name+"println(\""+txt[index+1]+"\")"+n)
        case "comb":
            print("todo")
        case "stroke":
            file_c.write(indent+name+"write(\""+duden(txt[index+1])+"\")"+n)
        case "hold":
            file_c.write(indent+name+"press(\""+duden(txt[index+1])+"\")"+n)
        case "rel":
            file_c.write(indent+name+"release(\""+duden(txt[index+1])+"\")"+n)
        case "relall":
            file_c.write(indent+name+"releaseAll()"+n)
        case "wait":
            file_c.write(indent+"delay("+txt[index+1]+")"+n)
        case "rep":
            file_c.write(indent+"while(1) {"+n)
            indent = indent + "    "
        case _:
            print("Befehl nicht erkannt: "+txt[index])

if indent == "        ":
    file_c.write("    }")
file_c.write("}")
file_c.close()



