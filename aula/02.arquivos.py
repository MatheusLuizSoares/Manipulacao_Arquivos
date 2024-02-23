arqui=open('arquivo.txt', 'w', )
arqui.write("Caio\nMarcos\nJoão\n")
#write serve quando tem uma somente string
# arqui.writelines()
#writelines server quanto tem multiplos strings,exemplo lista
x=["Caio","João","Marcos"]
arqui.writelines(x)
arqui.close()


