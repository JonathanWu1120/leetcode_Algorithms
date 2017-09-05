class Solution {
    public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;
        for(int i = 0; i < moves.length();i++){
            char a = moves.charAt(i);
            if(a == 'U') x++;
            else if(a  == 'D') x--;
            else if(a == 'L') y++;
            else if(a == 'R') y--;
        }
        return(x == 0 && y == 0);
    }
}