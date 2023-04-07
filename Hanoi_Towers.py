# TASK:
#
# Please read: https://en.wikipedia.org/wiki/Tower_of_Hanoi

# disks stacked on one rod in order of decreasing size, the smallest at the top
Towers = [[5, 4, 3, 2, 1],
    [],
    []
]

Bashni = [
    [],
    [],
    [5, 4, 3, 2, 1]    
]

def reshit():
    print("Welcome to Hanoi Towers", Bashni)
    hod_otkuda = int(input("Hoditj otkuda? ==>:"))
    hod_chto = int(input("Hoditj chem? ==>:"))
    hod_kuda = int(input("Hoditj kuda? ==>:"))

    # Если размер одной из башень(0[],1[],2[]) равен нулю(0), то нечем ходить
    if len(Bashni[hod_otkuda])==0:
        print("Nechem hoditj")
        return False
    # После первого хода выбора массива, мы выбираем елемент массива,
    # И этот выбор НЕ евляется минимальным индексом этого массива, то нельзя им ходить
    if hod_chto !=min(Bashni[hod_otkuda]):
        print("Ty ne mozhesh hoditj etim kruglishkom")
        return False
    # Если размер масива равен 0, то можно поместить первый элемент hod_otkuda[hod_chto] => hod_kuda[hod_chto]
    elif len(Bashni[hod_kuda])==0:
        Bashni[hod_kuda].append(hod_chto)
        Bashni[hod_otkuda].remove(hod_chto)
    elif hod_chto < min(Bashni[hod_kuda]):
        Bashni[hod_kuda].append(hod_chto)
        Bashni[hod_otkuda].remove(hod_chto)
    else:
        print("You cannot move there")
        return False
    if (Bashni[2] == [5,4,3,2,1]) or (Bashni[1] == [5,4,3,2,1]):
        print("You have won!")
        return True

while True:
    reshit()
    




# The objective of the puzzle is to move the entire stack to the last rod, obeying the following rules:
#
# 1. Only one disk may be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3. No disk may be placed on top of a disk that is smaller than it.

# please implement function to solve to puzzle