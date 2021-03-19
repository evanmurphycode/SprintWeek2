{"filter":false,"title":"Backpack.py","tooltip":"/Backpack.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":74,"column":0},"action":"insert","lines":["def ValidText(TextValue):","","    IsValid = True","    allowed_char = set(\"ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'\")","    if TextValue == \"\":","        print(\"Invalid input - value cannot be blank.\")","        IsValid = False","    elif set(TextValue).issubset(allowed_char) == False:","        print(\"Invalid input - entry contains invalid character.\")","        IsValid = False","","    return IsValid","","def ValidInteger(IntegerValue):","","    IsValid = True","    if IntegerValue == \"\":","        print(\"Invalid input- value cannot be blank.\")","        IsValid = False","    elif IntegerValue.isdigit() == False:","        print(\"Invalid input - value must be numbers only.\")","        IsValid = False","","    return IsValid","","","def ValidPhone(PhoneValue):","","    IsValid = True","    if PhoneValue.isdigit() == False:","        print(\"Invalid input - value must be numbers only - no spaces.\")","        IsValid = False","    elif len(PhoneValue) != 10:","        print(\"Invalid input - must be 10 digits.\")","        IsValid = False","","    return IsValid","","def ValidIntegerNumber(NumberValue, MinValue, MaxValue):","","    IsValid = True","    try:","        NumberValue = int(NumberValue)","    except:","        print(\"Invalid input - must be a valid number.\")","        IsValid = False","    else:","        if NumberValue < MinValue or NumberValue > MaxValue:","            print(\"Invalid input - number must be between \" + str(MinValue) + \" and \" + str(MaxValue) + \".\")","            IsValid = False","","    return IsValid","","","def ValidFloatNumber(NumberValue, MinValue, MaxValue):","","    IsValid = True","    try:","        NumberValue = float(NumberValue)","    except:","        print(\"Invalid input - must be a valid number.\")","        IsValid = False","    else:","        if NumberValue < MinValue or NumberValue > MaxValue:","            print(\"Invalid input - number must be between \" + str(MinValue) + \" and \" + str(MaxValue) + \".\")","            IsValid = False","","    return IsValid","","def StrAndPad(DollarValue):","    DollarValueStr = \"${:,.2f}\".format(DollarValue)","    DollarValuePad = \"{:>10}\".format(DollarValueStr)","","    return DollarValuePad",""],"id":1}]]},"ace":{"folds":[],"scrolltop":1112,"scrollleft":0,"selection":{"start":{"row":55,"column":0},"end":{"row":55,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1616179499624,"hash":"9378ae35ae8f35a3d4ff1fc9cc036a4547dc4516"}