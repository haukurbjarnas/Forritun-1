class Island():

    def __init__(self, n):

        self.grid_size = n
        self.grid = []
        for i in range(n):
            row = [0]*n
            self.grid.append(row)
    
    def __str__(self):

        s = ""
        for j in range(self.grid_size-1, -1, -1):
            for i in range(self.grid_size):
                if not self.grid[i][j]:
                    s+= "{:<2s}".format('.' + "  ")
                else:
                    s+= "{:<2s}".format((str(self.grid[i][j])) + "  ")
            s+="\n"
        return s