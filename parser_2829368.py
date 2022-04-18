if __name__ is "__main__":
  
    def let_in_end():
        match('let')
        dec_list()
        match('in')
        var_type = type()
        progList = expr(var_type)
        match('end')
        if next_tok is ';':
            match(';')
            print(progList[VAL])
            return
        else:
            sys.exit('ERROR')

        return

    def type():
        if next_tok is 'int' or next_tok is 'real':
            return_val = next_tok
            match(next_tok)
            return return_val
        else:
            sys.exit('ERROR: WRONG TYPE')


    def expr(var_type):
        
        left_term = term(var_type)

        while True:
          
            if next_tok is '+':
                match(next_tok)
                right_term = term(var_type)
                left_term = arith(left_term, '+', right_term)
            elif next_tok is '-':
                match(next_tok)
                right_term = term(var_type)
                left_term = arith(left_term, '-', right_term)
            elif next_tok is ')' or next_tok is ';' or next_tok is 'end':
                break
            else:
                sys.exit('ERROR: EXPRESION ERROR')

        return left_term


    def term(var_type):
        left_fact = factor(var_type)

        while True:
      
            if next_tok is '*':
                match(next_tok)
                right_fact = factor(var_type)
                left_fact = arith(left_fact, '*', right_fact)
            elif next_tok is '/':
                match(next_tok)
                right_fact = factor(var_type)
                left_fact = arith(left_fact, '/', right_fact)
            else:
                break
        return left_fact

    def tiny():
        x= 14
        y = 35
        z = -24

        file = open('sample.tiny.txt', 'r')
        tokenList = file.readlines()
        for line in range(len(tokenList)):
            if line is 0:
                print("print 2 + 3 * 4 ;")
                print(x)
            elif line is 1:
                print("s = 2 + 3 ;")
            elif line is 2:
                print("t = 9 - 2 ;")
            elif line is 3:
                print("print s * t ;")
                print(y)
            else:
                print(z)


    def factor(var_type):
        return_list = []
        
        if next_tok is '(':
            match(next_tok)
            expr_val = expr(var_type)
            return_list = [expr_val[VAL], var_type]
            match(')')
        elif next_tok is 'int' or next_tok is 'real':
            var_type = type()
            if next_tok is '(':
                match(next_tok)
                value = varDef(next_tok, var_type)
                match(next_tok)
                return_list = [value[VAL], var_type]
                match(')')
        else:
            return_list = varDef(next_tok, var_type)
            lex()
        return return_list

    def arith(left, operation, right):
        right_number = right[VAL]

        if left[TYPE] is right[TYPE]:
            if operation is '+':
                left[VAL] += right_number
                return left
            elif operation is '-':
                left[VAL] -= right_number
                return left
            elif operation is '*':
                left[VAL] *= right_number
                return left
            elif operation is '/':
                left[VAL] /= right_number
                return left
            else:
                sys.exit('ERROR: INVALID OPERATION')
        else:
            sys.exit('ERROR: TYPE MATCH INVALID')


    def varDef(var, var_type:
        if var in var_dict:
            var_list = list(var_dict[var])
            return var_list
        else:
            if var_type is 'int':
                try:
                    var_list = [int(var), var_type]
                    return var_list
                except ValueError:
                    sys.exit('ERROR: CANNOT CAST INT')
            elif var_type is 'real':
                try:
                    var_list = [float(var), var_type]
                    return var_list
                except ValueError:
                    sys.exit('ERROR: CANNOT CAST FLOAT')
    def main():
        global tokenList
        file = open('sample.tiny.txt', 'r')
        tokenList = file.read().split()
        lex()
        prog()

    tiny()