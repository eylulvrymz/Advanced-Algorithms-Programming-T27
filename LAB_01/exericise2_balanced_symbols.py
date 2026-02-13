def balance_bracks (s):
    #stack to keep track of the opened brackets
    stk_opened = []
    # for counting the comparisons
    comp_count = 0
    open_brac_list = ['(','[','{']
    close_brac_list = [')', ']', '}']
    matches = {')':'(',']':'[','}':'{'}
    for brac in s:
        if brac in open_brac_list:
            stk_opened.append(brac)
        elif brac in  close_brac_list:
            comp_count+=1
            if stk_opened == []:
                return False, comp_count
            last_brac = stk_opened.pop()
            if matches [brac]!= last_brac:
                return False, comp_count
    if len(stk_opened) == 0:
        return True,comp_count
    else:
        return False, comp_count
        
#testing
print("Test 1 (Balanced):", balance_bracks("({[]})"))
print("Test 2 (Empty):", balance_bracks(""))
print("Test 3 (No Opener):", balance_bracks("]"))
print("Test 4 (Leftover):", balance_bracks("((("))
