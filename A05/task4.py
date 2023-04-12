class MyGroceryList:
    def __init__(self, mylist):
        self.list = mylist

    def __getitem__(self, index):
        if(index<len(self.list)):
            return self.list[index]
        else:
            return self.list[len(self.list) - 1]
        
    def __delitem__(self, index):
        if(index<len(self.list)):
            del self.list[index]
        else:
            del self.list[len(self.list) - 1]
    
    def len(self):
        return len(self.list)

l = MyGroceryList(['Carrots', 'chicken', 'tomatoes', 'bread'])
print(l[1])
print(l[20])
print("\n")
del l[0]
for i in range(l.len()):
    print(l[i])
del l[20]

print("\n")

for i in range(l.len()):
    print(l[i])

