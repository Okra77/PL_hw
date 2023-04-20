'''
狀態    id    +    *     (     )    $      E   T   F
0       S5              S4                 1   2   3
1            S6                    acc
2            R2    S7         R2    R2
3            R4    R4         R4    R4
4       S5              S4                 8   2   3
5            R6    R6         R6    R6
6       S5              S4                     9   3
7       S5              S4                         10
8            S6               S11
9            R1    S7         R1    R1
10           R3    R3         R3    R3
11           R5    R5         R5    R5
1. E -> E + T
2. E -> T
3. T -> T * F
4. T -> F
5. F -> ( E )
6. F -> id
'''
# 定義文法
rules = {
    1: ("E", "E+T"),
    2: ("E", "T"),
    3: ("T", "T*F"),
    4: ("T", "F"),
    5: ("F", "(E)"),
    6: ("F", "id")
}

# 定義解析表
action = {
    0: {"id": "S5", "(": "S4", "E": "1", "T": "2", "F": "3"},
    1: {"+": "S6", "$": "acc"},
    2: {"+": "R2", "*": "S7", ")": "R2", "$": "R2"},
    3: {"+": "R4", "*": "R4", ")": "R4", "$": "R4"},
    4: {"id": "S5", "(": "S4","E": "8", "T": "2", "F": "3"},
    5: {"+": "R6", "*": "R6", ")": "R6", "$": "R6"},
    6: {"id": "S5", "(": "S4", "T": "9", "F": "3"},
    7: {"id": "S5", "(": "S4", "F": "10"},
    8: {"+": "S6", ")": "S11"},
    9: {"+": "R1", "*": "S7", ")": "R1", "$": "R1"},
    10: {"+": "R3", "*": "R3", ")": "R3", "$": "R3"},
    11: {"+": "R5", "*": "R5", ")": "R5", "$": "R5"}
}
#id+id*id
def shift_reduce_parser(tokens:list):
    stack = [0]
    symbol_stack = ['$']


    while True:
        state = stack[-1]
        token = tokens[0]
        
        if token not in action[state]:
            return "Error"
            
        action_entry = action[state][token]
            
        if action_entry == "acc":
            return "Accept"
        elif action_entry[0] == "S":
            symbol_stack.append(tokens[0])
            tokens.pop(0)
            state = int(action_entry[1:])
            stack.append(state)

        elif action_entry[0] == "R":
            rule_num = int(action_entry[1:])
            lhs, rhs = rules[rule_num]
            for j in range(len(rhs)):
                stack.pop()
                symbol_stack.pop()
                    
            state = stack[-1]
            symbol_stack.append(lhs)
            if lhs not in action[state]:
                return "Error"
            else:
                stack.append(int(action[state][lhs]))
            
        elif action[state] == "E" or "T" or "F":
            state = int(action_entry)
            stack.append(state)
            


        else:
            return "Error"

    
    '''while True:
        try:
            state = stack[-1]
            token = tokens[i]
            print(stack)
            print(symbol_stack)
            if token not in action[state]:
                return "Error"
            
            action_entry = action[state][token]
            
            if action_entry == "acc":
                return "Accept"
            elif action_entry[0] == "S":
                state = int(action_entry[1:])
                stack.append(state)
                symbol_stack.append(token)
                i += 1
            elif action_entry[0] == "R":
                rule_num = int(action_entry[1:])
                lhs, rhs = rules[rule_num]
                for j in range(len(rhs)):
                    stack.pop()
                    symbol_stack.pop()
                    i-=1
                    
                state = stack[-1]
                symbol_stack.append(lhs)
                if lhs not in action[state]:
                    return "Error"
                stack.append(int(action[state][lhs]))
            
            elif action[state] == "E" or "T" or "F":
                state = int(action_entry)
                stack.append(state)
                i+=1


            else:
                return "Error"
        except:
            return 'other error'
'''


while True:
    try:
        A = list(input())
        tokens = []
        for i in A:
            if i == 'i':
                tokens.append('id')
            elif i == '+':
                tokens.append('+')
            elif i == '*':
                tokens.append('*')
            elif i == '(':
                tokens.append('(')
            elif i == ')':
                tokens.append(')')
            
        
        tokens.append("$")
        result = shift_reduce_parser(tokens)
        print(result)


    except EOFError:
        break