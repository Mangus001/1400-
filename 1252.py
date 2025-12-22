text = input()
text_stripped = text.strip()
if text_stripped.startswith(('+','-','0','1','2','3','4','5','6','7','8','9')) and text_stripped.replace('.','',1).isdigit():
    print("Yes")
else:
    print("No")
