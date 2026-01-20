from interpreter import CommandInterpreter
def main():
    interpreter = CommandInterpreter()
    print("Simple Command Line Interpreter")
    print("Commands:")
    print("add x y")
    print("sub x y")
    print("exit")
    while True:
        user_input = input("enter input:")
        if user_input.lower()=="exit":
            print("Program closed")
            break
        result=interpreter.interpret(user_input)
        print(result)
if __name__=="__main__":
    main()
