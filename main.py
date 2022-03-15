def demp_zip():
   for a, b in zip(range(5,10), range(10,20,2)):
        print(a, b)
def demo_walrus():
    a =['spam','eggs']
    if a_len := len(a):
        print("a>0", a_len)
    else:
        print(a)

def main():
    demp_zip()
if __name__ == '__main__':
    main()