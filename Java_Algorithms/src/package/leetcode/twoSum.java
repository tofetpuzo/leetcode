import java.util.Arrays;
public class twoSum {
    public static void main(String[] args) {
        int[] num = {1, 2, 3, 4, 5, 9};
        int[] result  = twoSums(num, 9);
        System.out.println(Arrays.toString(result));
    }
    public static int[] twoSums(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
           for (int j = i+1; j < nums.length; j++) {
            if(nums[i] + nums[j] == target) {
                return new int[] {i , j};
             }
           }
       }  
       throw new IllegalArgumentException("No solution");
    }
}

