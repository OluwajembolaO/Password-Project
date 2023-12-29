specialChar = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
GoodToGo = True
NuhUh = False


def numCheck(pwd):
    numsUsed = []
    numCount = 0
    for i in pwd:
        if i in nums:
            numCount += 1
            numsUsed.append(i)
    if numCount < 2:
        return NuhUh
    else:
        for f in numsUsed:
            if numsUsed.count(f) > 1:
                return NuhUh
            else:
                return GoodToGo


def userNameInPwdCheck(pwd, userName):
    if userName in pwd:
        return NuhUh
    else:
        return GoodToGo


def specialCheck(pwd):
    for x in specialChar:
        f = 0
        if x in pwd:
            return GoodToGo
    return NuhUh


def pwdSubmission():
    # Placeholders had to make rPWD and PWD different before the loop in order for it to activate
    repeatPwd = ""
    pwd = "A"
    userName = "B"
    while repeatPwd != pwd:
        while len(pwd) < 10 or not numCheck(pwd) or not userNameInPwdCheck(pwd, userName) or not specialCheck(pwd):
            pwd = input("Enter a Password: ")
            userName = input("Enter your username: ")
            if len(pwd) < 10:
                print("PWD TOO SHORT TRY AGAIN!")
            if not numCheck(pwd):
                print("YOU NEED MORE NUMBERS OR YOU USED TWO OF THE SAME #")
            if not userNameInPwdCheck(pwd, userName):
                print("YOUR USERNAME IS IN YOUR PASSWORD >:(")
            if not specialCheck(pwd):
                print("YOU DIDNT USE ANY SPECIAL CHARACTERS!")

        repeatPwd = input("Whats your password again?: ")
        if repeatPwd != pwd:
            print(
                f"HAHA TOO bad! Your password was actually ({pwd}) . But you typed ({repeatPwd}). NOW YOU START ALL OVER AGAIN! YAY =)")
    print("Logged In Successfully")
    return pwd, userName


pwdSubmission()
