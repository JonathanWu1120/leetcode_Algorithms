/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i;
    int j;
    int *var = (int)malloc(sizeof(int) * 2);//allocates memory of size eight for the array of two variables
    if(numsSize < 2){
        var[0] = 0;
        var[1] = 0;
    }
    for(i = 0; i < numsSize;i++){
        for(j=1+i; j < numsSize;j++){
            if(nums[i]+nums[j] == target){
                var[0] = i;
                var[1] = j;
            }
        }
    }
    return var;
}