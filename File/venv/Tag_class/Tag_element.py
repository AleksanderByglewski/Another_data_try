
import pickle

class Element():
    def __init__(self, name,tag_list,email_list):
        self.name=name
        email_list=[]
        tag_list=[]
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
class Tag_Element():
    def __init__(self,x,y):
        super.__init__(x,y,z='')