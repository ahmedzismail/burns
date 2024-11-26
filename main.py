#دالة نسبة الحروق
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
  هذا البرنامج لقياس نسبة الحروق في الجسم حسب قاعدة التسعات
      Rule of nines
                تعليمات البرنامج
  من فضلك ادخل اسم المنطفة المصابة بالحرق باللغة الانجليزية
                     الراس= head = 9%
                     الذراع الواحد= arm =9%
                     الساق الواحدة = leg = 18%
                     الجذع الامامي= anterior trunk = 18%
                     الجذع الخلفي= posterior trunk = 18%
                     الاعضاء التناسلية= genitalia = 1%
     في حالة مااذا كانت الاصابة في الذراعين  او الرجلين نكتب اسم العصو مرتين
  في حالة الانتهاء من الادخال قم بكتابة
  end
    """)
  while True:
    burn_area=input("""من فضلك  ادخل اسم العضو المصاب 
    head - arm - leg - anterior trunk - posterior trunk - genitalia - end 
    """).lower()
    if burn_area=="end":
     break
    elif burn_area in rule_of_nines.keys():
      burns_percen+=rule_of_nines[burn_area]
    else:
         print(" wrong choice try again "+"ادخال خاطىء  اعد المحاولة")
  print(f"the total burns area is { burns_percen}%")
burns_percent()
    
