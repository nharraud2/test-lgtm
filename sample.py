li = [1, 2, 3]

for elt in li:
    elt + "test"  # Should fail

assert(1, "message 2")  # Assert on tuple



from tempfile import mktemp
def write_results(results):
    filename = mktemp()
    with open(filename, "w+") as f:
        f.write(results)
    print("Results written to", filename)


#Cannot raise an int, even if we want to
def raise_int():
    #Will raise a TypeError
    raise 4

    
a_list = []
a_list()

b_list = [round]
b_list[0]()

c_list = [1]
c_list[0]()

def annotated(param: int):
    param()
