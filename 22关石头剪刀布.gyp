import random

choices = ['石头', '剪刀', '布']

win=[
  ('石头','剪刀'),
  ('布','石头'),
  ('剪刀','布')
    ]

your_choice = input('请输入石头、剪刀或布')

if your_choice in choices:
  computer_choice=random.choice(choices)
  if [your_choice,computer_choice] in win:
    print('你出了%s,电脑出了%s，你赢了' %(your_choice,computer_choice))
    
  elif your_choice==computer_choice:
    print('你出了%s,电脑出了%s，平局' %(your_choice,computer_choice))
    
  else:
    print('你出了%s,电脑出了%s，你输了' %(your_choice,computer_choice))

else:
  print('输入格式错误')