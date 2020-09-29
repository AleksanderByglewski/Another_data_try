class Element():

    def __init__(self, name='', tag_list=None, email_list=None):
        self.specializer(name, tag_list, email_list)
        # Apply the Kiss principle, okay big guy?

    def specializer(self, name='', tag_list=None, email_list=None):
        self.name = name
        self.tag_list = []
        self.email_list = []
        if tag_list is not None:
            self.tag_list = tag_list
        if email_list is not None:
            self.email_list = email_list

    def __repr__(self):
        expr = self.name
        expr += ' ['
        special_sep = ''
        for tag in self.tag_list:
            expr += special_sep + tag
            special_sep = ','
        expr += '] ['
        special_sep = ''
        for email in self.email_list:
            expr += special_sep + email
            special_sep = ','
        expr += ']'
        return (expr)

    def join(self, partner):
        self.tag_list.extend(partner.tag_list)
        self.email_list.extend(partner.email_list)

    def read_in(self, line):
        line=line.rstrip()
        list_line = line.split(' ')
        name_to_pass = list_line[0]
        self.name = name_to_pass
        tag_list = (list_line[1][1:-1]).split(',')
        email_list = (list_line[2][1:-1]).split(',')
        dead_friend = Element(name_to_pass, tag_list, email_list)
        self.join(dead_friend)
    def __eq__(self, other):
        if(self.name==other.name):
            return True
        return False

line = 'DECIMUS_MERIDIUS [GENERAL,GLADIATOR] [WIFE,SON]'
The_gladiator = Element()


#The_gladiator.read_in(line)
#with open('split_the_grave.txt', 'r') as f:
#    line_containing_data=f.readline()
#    line_containing_data=line_containing_data.rstrip()
#    The_gladiator.read_in(line_containing_data)

#    print(The_gladiator)

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
        for other_Gladiator in the_list_of_gladiators[(index+1):]:
            if other_Gladiator.name==tag_for_deletion:
                continue
            if current_Gladiator==other_Gladiator:
                current_Gladiator.join(other_Gladiator)
                other_Gladiator.name=tag_for_deletion
    deletion(the_list_of_gladiators,tag_for_deletion)
def deletion(the_list_of_gladiators, eraser_tag):
    return [x for x in the_list_of_gladiators if x.name!=eraser_tag]
    #print(the_list_of_gladiators)


the_list_of_gladiators=read_them_out('split_the_grave.txt')
consolidate_gladiators(the_list_of_gladiators)

with open('grave.txt', 'w') as f:
    for gladiator in the_list_of_gladiators:
        f.write(str(gladiator))
        f.write('\n')

class Tag_Element():
    def __init__(self, x, y):
        super.__init__(x, y, z=None)

