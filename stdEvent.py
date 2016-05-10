categories = {'None' : 0, 'Academic' : 1, 'Arts' : 2, 'Athletics' : 3, 'Exhibits' : 4, 'Community' : 5, 'Religious' : 6, 'Student Life' : 7, 'Alumni' : 8, "Lectures" : 9}
categoryNames = ['None', 'Academic', 'Arts', 'Athletics', 'Exhibits', 'Community', 'Religious', 'Student Life', 'Alumni', "Lectures"]
class stdEvent :
    def __init__ (self, n, d, c) :
        self.name = n
        self.description = d
        self.category = c
        
