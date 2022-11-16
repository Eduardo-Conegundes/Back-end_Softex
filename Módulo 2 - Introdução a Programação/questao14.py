class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def getTitle(self):     
        print ("title accessed")
        return self.title

    def getDescription(self):      
        print ("description accessed")
        return self.description

    def getCompleted(self):       
        print ("completed accessed")
        return self.completed

    def setTitle(self, newtitle):
        print ("title changed")
        if type(newtitle) == str:
            self.title = newtitle
        else:
            print ("invalid value title changed")
            self.title = None

    def setDescription(self, newdescription):
        print ("description changed")
        if type(newdescription) == str:
            self.description = newdescription
        else:
            print ("invalid value description changed")
            self.description = None

    def setCompleted(self, newbool):
        print ("completed changed")
        if type(newbool) == bool:
            self.completed = newbool
        else:
            print ("invalid value completed changed")
            self.completed = None
