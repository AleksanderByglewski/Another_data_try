# This is a sample Python script.
from Tag_class.Tag_element import Element
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def read_them_out(filename):
    list=[]
    with open(filename,'r') as f:
        for line in f:
            The_gladiator=Element()
            The_gladiator.read_in(line)
            list.append(The_gladiator)
    return list

def consolidate_gladiators(the_list_of_gladiators, tag_for_deletion="PROCESSED_AND_PENDING_FOR_DELETION"):
    for index,current_Gladiator in enumerate(the_list_of_gladiators):
        if(index>10000):
            break
        for other_Gladiator in the_list_of_gladiators[(index+1):]:
            if(index%100==0):
                print(index)

            try:
                if other_Gladiator.name==tag_for_deletion:
                    continue
                if current_Gladiator==other_Gladiator:
                    current_Gladiator.join(other_Gladiator)
                    other_Gladiator.name=tag_for_deletion
            except Exception as error:
                print("This has occured %s", error)
    return deletion(the_list_of_gladiators,tag_for_deletion)
def deletion(the_list_of_gladiators, eraser_tag):
    return [x for x in the_list_of_gladiators if x.name!=eraser_tag]
    #print(the_list_of_gladiators)



def bind_on_the_basis_of_comp(f1,f2,a,b):
    if(f1(a)==f2(b)):
        a.imbue_with_tag(b)

# Press the green button in the gutter to run the script.
print_hi('PyCharm')
line = 'DECIMUS_MERIDIUS [GENERAL,GLADIATOR] [WIFE,SON]'
The_gladiator = Element()
the_list_of_gladiators = read_them_out('Tag_class/split_the_grave.txt')
the_list_of_gladiators = consolidate_gladiators(the_list_of_gladiators)
with open('grave.txt','w') as f:
    for gladiator in the_list_of_gladiators:
        print(str(gladiator))
        f.write(str(gladiator))
        f.write('\n')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
