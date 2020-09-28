
class Element():
    def __init__(self, name='',tag_list=None,email_list=None):
        specializer()
    def specializer(self, name='',tag_list=None,email_list=None):
        self.name=name
        tag_list=[]
        email_list=[]
        if tag_list is not None:
            self.tag_list=tag_list
        if email_list is not None:
            self.tag_list = email_list

        #Apply the Kiss principle, okay big guy?

    def __repr__(self):
        expr=self.x
        expr+=' ['
        for tag in self.tag_list:
            expr+=tag
        expr+='] ['
        for email_list in self.email.list:
            expr+=email_list
        expr+=']'
        return(expr)
    def join(self,partner):
        self.tag_list.extend(partner.tag_list)
        self.email_list.extend(partner.email_list)
    def read_in(line):
        list_line=line.split(' ')
        name_to_pass=list_line[0]
        tag_list=(list_line[1][1:-1]).split(' ')
        email_list=(list_line[2][1:-1]).split(' ')
        dead_friend=Element(name.x,tag_list,email_list)
        self.join(dead_friend)


class Tag_Element():
    def __init__(self,x,y):
        super.__init__(x,y,z=None)