def getSym(v):
  if v:
    return 'T'
  else: 
    return 'F'
vals = [True, False]
print('+----------------------------------+')
print('|         and Truth Table          |')
print('+----------------------------------+')
for A in vals:
 for B in vals: 
  print('| A = ',getSym(A),  ' B = ', getSym(B), ' | ', 'A ^ B = ', getSym(A and B),' |')
print('------------------------------------')
print('+----------------------------------+')
print('|          or Truth Table          |')
print('+----------------------------------+')
for A in vals:
 for B in vals: 
  print('| A = ',getSym(A),  ' B = ', getSym(B), ' | ', 'A v B = ', getSym(A or B),'  |')
print('------------------------------------')
print('------------------------------------')
print('+----------------------------------+')
print('|          ^ Truth Table        |')
print('+----------------------------------+')
for A in vals:
 for B in vals: 
  print('| A = ',getSym(not A),  ' B = ', getSym(not B), ' | ', 'A ^ B = ', getSym(A or B),'|')
print('------------------------------------')
print('+----------------------------------+')
print('|           ~ Truth Table        |')
print('+----------------------------------+')
for A in vals:
 for B in vals: 
  print('||| A = ',getSym(not A),  ' B = ', getSym(not B), ' || ', 'A ~v B = ', getSym(A and B),' |')
print('------------------------------------')
print('+----------------------------------+')
print('|           or Truth Table        |')
print('+----------------------------------+')
for A in vals:
 for B in vals: 
  print('| A = ',getSym(A),  ' B = ', getSym(B), ' | ', 'A ~v B = ', getSym(A != B),' |')
print('------------------------------------')
print('+----------------------------------+')
print('|         ~ Truth Table          |')
print('+----------------------------------+')
for A in vals:
 for B in vals: 
  print('| A =',getSym(A),  ' ~A =', getSym(not A), ' | ', ' B =', getSym(B),' ~B =', getSym(not B),'|')
print('------------------------------------')