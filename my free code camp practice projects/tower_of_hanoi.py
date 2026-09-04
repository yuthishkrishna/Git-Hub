def hanoi_solver(disks):
    one = [i for i in range(disks, 0, -1)]
    two = []
    three = []
    
    def get_the_list():
        return f'{one} {two} {three}\n'
    
    def move_the_disk(start, target):
        if not start:
            return
        target.append(start.pop())

    def move_the_tower(start, target, auxillary, disks):
        if disks == 1:
            move_the_disk(start, target)
            return get_the_list()

        result = ""
        result += move_the_tower(start, auxillary, target, disks - 1)

        move_the_disk(start, target)
        result += get_the_list()

        result += move_the_tower(auxillary, target, start, disks - 1)
        return result

    return_string = get_the_list()
    if disks > 0:
        return_string += move_the_tower(one, three, two,disks )
        return return_string.rstrip("\n")
a= int(input("Enter the number of disks: "))
print(hanoi_solver(a))