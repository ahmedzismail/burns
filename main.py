from flet import *
def burns_percent():
  rule_of_nines={
    "head":9,
    "arm":9,
    "leg":18,
    "anterior trunk":18,
    "posterior trunk":18,
    "genitalia":1,
  }
  burns_percen=0
  print(""""
  this program to calculate burns surface area using
               Rule of nines
          instructions

          head = 9%
          one arm =9%
          one leg = 18%
          anterior trunk = 18%
          posterior trunk = 18%
          genitalia = 1%
      """)
  while True:
    burn_area=input(""" Enter your choice of burn area
    head - arm - leg - anterior trunk - posterior trunk - genitalia - end 
    """).lower()
    if burn_area=="end":
     break
    elif burn_area in rule_of_nines.keys():
      burns_percen+=rule_of_nines[burn_area]
    else:
         print(" wrong choice try again ")
  print(f"the total burns area is { burns_percen}%")
burns_percent()
