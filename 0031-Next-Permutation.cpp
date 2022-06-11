class Solution {
public:
void nextPermutation(vector& nums) {

    /*Step and intituitions to be followed:
    
    Step 1: Find a break point from last where a single element is not in incresing order 
        i.e, ar[i] < ar[i+1] and keep that index such as ind1
    
    Step 2: Find again from last that which element is just greater than ind1 
        as to follow the dictionary order to place bigger element than ind1 and name ind2
        
    Step 3: Swap ar[ind1] and ar[ind2]
        
    Step 4: Reverse from the next elemnt of ind1 i.e, ind1 + 1 to last of the array
        
    Edge Case: If the array is already increasing order from the last then just reverse it. */
    
    int n = nums.size();
    int k; //to find break point
    int l; // to traverse from last and find the greater element han break point
    
    for(k=n-2; k>=0; k--) //step 1
    {
        if(nums[k] < nums[k+1])
            break;
    }
    
    if(k < 0) //edge case
        reverse(nums.begin(), nums.end());
    else
    {
        for(l=n-1; l>k; l--) //step 2
        {
            if(nums[l] > nums[k])
                break;
        }
        
        swap(nums[k], nums[l]); //step 3
    
        reverse(nums.begin() + k + 1, nums.end()); //step 4
    }              

}
};