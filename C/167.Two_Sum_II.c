/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int i;
    int j;
    int *var = (int)malloc(sizeof(int) * 2);
    if(numbersSize<2){
        *returnSize = 0;
        return var;
    }
    i = 0;
    j = numbersSize - 1;
    while(true){
        if(numbers[i]+numbers[j] > target){
            j--;
        }else if(numbers[i]+numbers[j] < target){
            i++;
        }else if(numbers[i]+numbers[j] == target){
            var[0] = i+1;
            var[1] = j+1;
            *returnSize = 2;
            return var;
        }
    }
}