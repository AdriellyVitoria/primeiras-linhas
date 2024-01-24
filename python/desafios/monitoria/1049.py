palavra1 = input().lower().strip()
palavra2 = input().lower().strip()
palavra3 = input().lower().strip()

if palavra1 == 'vertebrado':
  if palavra2 =='ave':
    if palavra3 =='carnivoro':
      print(f'aguia')
    elif palavra3 == 'onivoro':
      print(f'pomba')
  elif palavra2 =='mamifero':
    if palavra3 =='onivoro':
      print(f'homem')
    elif palavra3 == 'herbivoro':
      print(f'vaca')
elif palavra1 == 'invertebrado':
  if palavra2 == 'inseto':
    if palavra3 == 'hematofago':
      print(f'pulga')
    elif palavra3 == 'herbivoro':
      print(f'lagarta')
  elif palavra2 =='anelidio':
    if palavra3 == 'hematofago':
      print(f'sanguessuga')
    elif palavra3 == 'onivoro':
      print(f'minhoca')