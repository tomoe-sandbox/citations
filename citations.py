# def main():
casenames = []
citations = []

active = True
while active:
    user_input = input("Please input your complete case citation here, Quit to exit: ")
    # if input is Quit, then exit
    if user_input == 'Quit':
        print(casenames)
        print(citations)
        active = False
        break
    else:
        # get citations
        for i in range(len(user_input)):
            if (i+1)<len(user_input) and user_input[i+1] == '[':
                casename = user_input[:i]
                cite= user_input[i+1:]
                casenames.append(casename)
                citations.append(cite)
                print(casename + ', ' + cite)
# user_input = input("Please input your complete case citation here, Quit to exit: ")
# for i in range(len(user_input)):
#             if (i+1)<len(user_input) and user_input[i+1] == '[':
#                 casename = user_input[:i]
#                 cite= user_input[i+1:]
#                 print(casename + ', ' + cite)


# #  Don't touch this
# if __name__ == "__main__":
#     main()

# If I put in CASE1, CASE2 and Quit, it should give me an output of...
