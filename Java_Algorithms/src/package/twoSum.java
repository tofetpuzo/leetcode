import java.lang.reflect.Array;
import java.util.Arrays;

public class twoSum {

    public static void main(String[] args) {
        int[] nums = {1, 2, 3, 4, 5, 9};
        twoSums(nums, 2);
    }
    public static int[] twoSums(int[] nums, int target) {
        int[] n = null;
        for (int i = 0; i < nums.length; i++) {
            Arrays.sort(nums);
            if(i > 0  && nums[i] == nums[i -1]) {
                continue;
            }
            int left = 0, res = 0, right = nums.length;


            
            System.out.println(nums[i]);
    
       }
        return n;    
    }
}
