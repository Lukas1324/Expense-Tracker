class AusgabenDTO:
    def __init__(self, id, amount, content, date, created_at):
        self.id = id
        self.amount = amount
        self.content = content
        self.date = date
        self.created_at = created_at
       
    def getId(self):
        return self.id
    
    def getAmount(self):
        return self.amount
    
    def getContent(self):
        return self.content
    
    def getDate(self):
        return self.date
    
    def getCreatedAt(self):
        return self.created_at
    