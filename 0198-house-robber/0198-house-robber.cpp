class Solution {
public:
    int rob(vector<int>& nums) {
        int size=nums.size();

        //base case
        if(size==1){
            return nums[0];
        }
        //array for max loot at each position
        int max_loot[size];

        //case for two elements in array;
        max_loot[0]=nums[0];
        max_loot[1]=max(nums[0],nums[1]);


        //case for more than two elements
        for(int i=2; i<size; i++){
            max_loot[i]=max(max_loot[i-2]+nums[i], max_loot[i-1]);
        }

        return max_loot[size-1];
    }
};