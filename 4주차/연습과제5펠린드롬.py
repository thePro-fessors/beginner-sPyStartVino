input = input()
re = False
len = len(input)


for i in range(len // 2):
   if input[i] == input[-1-i]:
      re = True
   else: 
     re = False
     break

print(f'{input} 은 펠린드롬인가요? {re}')