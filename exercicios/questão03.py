with open('exercicios/frutas.txt','r') as arqui:
 quant_frutas=0
 
 for linha in arqui:
  fruta=linha.strip()
 
  print(fruta)
  
  quant_frutas+=1
  
print(f'\nQuantidade de frutas:{quant_frutas}')