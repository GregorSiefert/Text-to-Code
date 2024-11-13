
crack_name = "test"

file_t_dir = "./Text/"+crack_name+"_T.txt"

file_t = open(file_t_dir,"r")

print(file_t.read(1))
print(file_t.read(1))   #Leerzeichen zählen auch als Zeichen
print(file_t.readline())