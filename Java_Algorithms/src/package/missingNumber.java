public class missingNumber {

    public static void main(String[] args) {
        int [] intArray = {1, 2, 3, 4, 5, 6, 8, 9, 10};
        System.out.println(missingNumbers(intArray));
    }
    public static int missingNumbers(int [] intArray) {
        int missingNumber = 0;
        for (int i = 1; i < intArray.length; i++) {
            for (int j = intArray.length - 1; j >= i; j--) {
                int no = (j / i);
                missingNumber = (missingNumber += no) % 10;
                
            }
            
        }
        return missingNumber;
        
    }

    // public static void missingNumberas(int[] intArray) {
    //     int sum1 = 0;
    //     int sum2 = 0;
    //     for (int i : intArray) {
    //         sum1 += i;         
    //     }
    //     sum2 = intArray.length*(intArray.length+1)/2;
    //     int diff = sum2 - sum1;
    //     System.out.println();

    // }
    
}
