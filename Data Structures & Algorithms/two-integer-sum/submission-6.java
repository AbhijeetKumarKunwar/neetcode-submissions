class Solution {
    
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hs=new HashMap<Integer,Integer>();
        int arr[]=new int[2];
        for(int i=0;i<nums.length;i++){
            int check=target-nums[i];
            if(hs.containsKey(check)){
             return new int[]{hs.get(check),i};

            }else
            {
                hs.put(nums[i],i);
            }
        }
        return new int[]{};

        
    }
}
