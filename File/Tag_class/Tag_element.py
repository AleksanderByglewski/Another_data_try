<<<<<<< HEAD
def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

class Element():
    def refit(self):
        self.tag_list=f7(self.tag_list)
        self.email_list=f7(self.email_list)

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
        self.refit()
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



#The_gladiator.read_in(line)
#with open('split_the_grave.txt', 'r') as f:
#    line_containing_data=f.readline()
#    line_containing_data=line_containing_data.rstrip()
#    The_gladiator.read_in(line_containing_data)

#    print(The_gladiator)


class Tag_Element():
    def __init__(self, x, y):
        super.__init__(x, y, z=None)

=======

class Element():

    def __init__(self, name='',tag_list=None,email_list=None):
        self.specializer(name,tag_list,email_list)
        #Apply the Kiss principle, okay big guy?

    def specializer(self, name='',tag_list=None,email_list=None):
        self.name=name
        self.tag_list=[]
        self.email_list=[]
        if tag_list is not None:
            self.tag_list=tag_list
        if email_list is not None:
            self.email_list = email_list
    def __repr__(self):
        expr=self.name
        expr+=' ['
        special_sep=''
        for tag in self.tag_list:
            expr+=special_sep+tag
            special_sep=','
        expr+='] ['
        special_sep=''
        for email in self.email_list:
            expr+=special_sep+email
            special_sep=','
        expr+=']'
        return(expr)
    def join(self,partner):
        self.tag_list.extend(partner.tag_list)
        self.email_list.extend(partner.email_list)
    def read_in(self,line):
        list_line=line.split(' ')
        name_to_pass=list_line[0]
        self.name=name_to_pass
        tag_list=(list_line[1][1:-1]).split(',')
        email_list=(list_line[2][1:-1]).split(',')
        dead_friend=Element(name_to_pass,tag_list,email_list)
        self.join(dead_friend)

line='DECIMUS_MERIDIUS [GENERAL,GLADIATOR] [WIFE,SON]'
The_gladiator=Element()
The_gladiator.read_in(line)
with open('grave.txt','w') as f:
    f.write(str(The_gladiator))
class Tag_Element():
    def __init__(self,x,y):
        super.__init__(x,y,z=None)
>>>>>>> master
