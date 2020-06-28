def compile(code):
    loop_code = ""
    loop = False
    memory = 0

    for i in range(len(code)):
        if loop == True and code[i] != ']':
            loop_code = loop_code + code[i]
        else:
            if code[i] == '+':
                memory = memory + 1
            if code[i] == '-':
                memory = memory - 1
            if code[i] == '.':
                print(memory)
            if code[i] == '/':
                print(chr(memory))
            if code[i] == '[':
                loop = True
        if code[i] == ']':
            loop_memory = int(memory)
            loop = False
            for i in range(loop_memory):
                for x in range(len(loop_code)):
                    if loop_code[x] == '+':
                        memory = memory + 1
                    if loop_code[x] == '-':
                        memory = memory - 1
                    if loop_code[x] == '.':
                        print(memory)
                    if loop_code[x] == '/':
                        print(chr(memory))
            loop_code = ""

compile("++++++++[++++++++]/[-]++++++++++[+++++++++]+/+++++++//+++/")