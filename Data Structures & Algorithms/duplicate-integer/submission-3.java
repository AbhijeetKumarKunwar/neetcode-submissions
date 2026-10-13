class Solution {
    public boolean hasDuplicate(int[] nums) {
        return Arrays.stream(nums).distinct().count()<nums.length;
    // HashSet<Integer> hs=new HashSet<>();
    // int flag=0;
    // for(int i=0;i<nums.length;i++){
    //     if(!hs.add(Integer.valueOf(nums[i]))){
    //         flag=1;
    //         break;

    //     }
          
    // }
    // if(flag==1)
    //   return true;
    //   else 
    //   return false;

        
    // }
}
}