class Solution {
    public int hammingDistance(int x, int y) {
        int z = x ^ y;
        String bin_str = Integer.toBinaryString(z);
        int count = 0;
        for(int i = 0; i < bin_str.length();i++){
            if(bin_str.charAt(i) == '1'){
                count ++;
            }
        }
        return(count);
    }
}