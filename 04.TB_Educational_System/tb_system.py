tb1 = {
    "first line":("isoniazid","rifmapin","pyrazinamide","ethambutol","sterptomycin"),
    "second line":{"fluroquinoles":("ofloxacin","levofloxacin","moxifloxacin","ciprofloxacin"),
                    "other oral drugs":("ethionamide","prothionamide","cycloserine","terizidone","para amino salicylic acid(PAS)","ribabutin","thiacetazone"),
                    "injectable":("kanamycin","amikacin","capreomycin")}
}


pre = {
    1:"if no resistance to TB drugs (both H and R senstitive  P and EB TB case",
    2:"clinically dignosed PTB ",
    3:"Complicated EP case (TB meningitis, neruological TB, bone TB,  non resolving lymph node",
    4:"if R if suceptible and INH resistance or unkown in bacteriologically confirmend PTB and EP-TB "
}


levo = (tb1['second line']['fluroquinoles'][1])
H = (tb1['first line'][0])
r= (tb1['first line'] [1])
e = (tb1['first line'][3])
z = (tb1['first line'][2])
med1 = []
for i in tb1['first line']:
     if i == tb1['first line'][4]:
      break
     med1.append(i)
med2 = []
for i in tb1['first line']:
  if i == tb1['first line'][2]:
    break
  med2.append(i)

print("!!!TB Diagnostic Centre !!!")
name = input("Enter your name:")
case = int(input("1.New case\n2.Treated case\nselect any one:"))

type = {
    1:"bacteriologically postive PTB patients",
    2:"bacteriologically negative PTB patinets",
    3:"extra-pulmpnary TB",
    4:"TB/HIV co - infected"
}

if case == 1:
  print("\"hello\"",name.capitalize())
  new_case = input("Are you never been treated for tb or have taken ATT for <1 month:Yes/No:  \n")
  if new_case == "yes":
    for i in  type:
      print(f"{i} {type[i]}")

    report = int(input("\nis your report include anything from above then select the number: "))
    match report:
      case 1|2|3|4:
       print(f"!!!Treatment regimen!!!\nIntensive phase (daily) 2(hrze){med1}\nContuation Phase(daily) 4(hr){med2}")
  else:
    print("Then you have to cheack up first for confirming TB")
else:
     for key,value in pre.items():
       print(f"{key} = {value}")
     symptom = int(input("\nare you phase any of this symptopm then select the number:"))
     match symptom:
        case 1:
            print(f"you need to take 6 {med1} daily")
        case 2:
            print(f"you need to take 6{med1} daily")
        case 3:
            print(f"you need to take 12 {med1}  + {levo} daily")
        case 4:
          print(f"You have to take 6 dose of {H} daily and {r} {e} {z} - {levo}  once")