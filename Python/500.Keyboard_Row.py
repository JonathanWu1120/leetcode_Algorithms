class Solution(object):
    def check_row(self,word,row,is_in_row):
        word = word.lower()
        for i in range(len(word)):
            is_in_row = is_in_row and (word[i] in row)
        return is_in_row
        
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = ["q",'w','e','r','t','y','u','i','o','p']
        row_2 = ['a','s','d','f','g','h','j','k','l']
        row_3 = ['z','x','c','v','b','n','m']
        arr = []
        for i in range(len(words)):
            is_in_row_1 = True
            is_in_row_2 = True
            is_in_row_3 = True
            a = words[i]
            if self.check_row(a,row_1,is_in_row_1):
                arr.append(a)
            elif self.check_row(a,row_2,is_in_row_2):
                arr.append(a)
            elif self.check_row(a,row_3,is_in_row_3):
                arr.append(a)
            #if in_row_1 == True or in_row_2 == True or in_row_3 == True:
            #    arr.append(a)
        return arr