
def twofer(name="you"):
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    if name.isalpha():
        return("One for {}, one for me.".format(name))
    else:
        return("One for you, one for me.")