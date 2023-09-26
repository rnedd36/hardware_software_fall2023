


def main():
    name = "Professor Nedd"
    print("We want to know if you like programming!")
    print()
    print("Do you like programming "+ name + "?")
    answer = input()
    print("Great! You said " + answer + "?")
    print("Let's learn some Python today")


# Since there is no main() function in Python, when the command to run a
# python program is given to the interpreter, the code that is at level 0
# indentation is to be executed. However, before doing that, it will define
# a few special variables. __name__ is one such special variable. If the source
# file is executed as the main program, the interpreter sets the __name__ variable
# to have a value “__main__”. If this file is being imported from another module,
# __name__ will be set to the module’s name. __name__ is a built-in variable
# which evaluates to the name of the current module. Thus it can be used to
# check whether the current script is being run on its own or being imported
# somewhere else by combining it with if statement, as shown below.
# Java runtime engine (jre)
# public static void main(String[] Args){}
# needs to be public so that it is callable outside the Class
# needs to be static so that the jre is able to call main without an instance
# it will be called on the actual class.
# void means it returns nothing.


if __name__ == "__main__":
    #print ("__name__ == %s" %__name__)
    main()
else:
    print ("%s is being imported" %__name__)
