def raddoppia_consonanti(stringa):

  nuova_stringa = ""
  vocali = "aàèéeiòoùu"

  for i, char in enumerate(stringa):
    if char in vocali:
      nuova_stringa += char
    else:
      nuova_stringa += char * 2
    if i == len(stringa) // 2:
      nuova_stringa += "o"
  return nuova_stringa

# Output
stringa = input("Inserisci una stringa: ")

nuova_stringa = raddoppia_consonanti(stringa)

print(f"Stringa originale: {stringa}")
print(f"Stringa con consonanti raddoppiate e 'o' nel mezzo: {nuova_stringa}")