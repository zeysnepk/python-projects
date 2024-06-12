"""
You have a file called “mails.txt” which contains emails and some text. Read each line of this file and print only the ones that fit the mail format.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com

                           //
                           //
                           //


*Tip: You can use the endswith and find methods on strings.*
"""



with open ("mails.txt","r") as mail:
    for i in mail:
        
        i = i[:-1]
        
        if i.endswith(".com"):
            if i.find("@"):
                print(i)
