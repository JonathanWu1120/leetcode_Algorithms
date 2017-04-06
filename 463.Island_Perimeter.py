class Solution(object):
    def up(self,grid,i,j):
        if grid[i-1][j] == 1:
            return -1
        else:
            return 0
    def down(self,grid,i,j):
        if grid[i+1][j] == 1:
            return -1
        else:
            return 0
    def left(self,grid,i,j):
        if grid[i][j-1] == 1:
            return -1
        else:
            return 0
    def right(self,grid,i,j):
        if grid[i][j+1] == 1:
            return -1
        else:
            return 0
    def top(self,*a):
        return (self.down(*a)+self.left(*a)+self.right(*a))
    def first(self,*a):
        return (self.up(*a)+self.down(*a)+self.right(*a))
    def last(self,*a):
        return (self.up(*a)+self.down(*a)+self.left(*a))
    def bottom(self,*a):
        return (self.up(*a)+self.left(*a)+self.right(*a))
    def center(self,*a):
        return (self.up(*a)+self.left(*a)+self.right(*a)+self.down(*a))
    def lr(self,*a):
        return (self.left(*a)+self.right(*a))
    def ud(self,*a):
        return (self.up(*a)+self.down(*a))
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                edges = 4
                a = (grid,i,j)
                if len(grid) == 1 and len(grid[0]) == 1:
                    if grid[i][j] == 1:
                        perimeter += 4
                    else:
                        perimeter += 0
                elif len(grid) == 1:
                    if j == 0:
                        if grid[i][j] == 1:
                            edges += self.right(*a)
                            perimeter += edges
                    elif j == len(grid[0])-1:
                        if grid[i][j] == 1:
                            edges += self.left(*a)
                            perimeter += edges
                    else:
                        if grid[i][j] == 1:
                            edges += self.lr(*a)
                            perimeter += edges
                elif len(grid[0]) == 1:
                    if i == 0:
                        if grid[i][j] == 1:
                            edges += self.down(*a)
                            perimeter += edges
                    elif i == len(grid)-1:
                        if grid[i][j] == 1:
                            edges += self.up(*a)
                            perimeter += edges
                    else:
                        if grid[i][j] == 1:
                            edges += self.ud(*a)
                            perimeter += edges
                elif grid[i][j] == 1:
                    if i == 0:
                        if j == 0:
                            edges += self.right(*a) + self.down(*a)
                        elif j == len(grid[0])-1:
                            edges += self.left(*a) + self.down(*a)
                        else:
                            edges += self.top(*a)
                        perimeter += edges
                    elif i == len(grid)-1:
                        if j == 0:
                            edges += self.up(*a) + self.right(*a)
                        elif j == len(grid[0])-1:
                            edges += self.up(*a) + self.left(*a)
                        else:
                            edges += self.bottom(*a)
                        perimeter += edges
                    else:
                        if j == 0:
                            edges += self.first(*a)
                        elif j == len(grid[0])-1:
                            edges += self.last(*a)
                        else:
                            edges += self.center(*a)
                        perimeter += edges
        return perimeter