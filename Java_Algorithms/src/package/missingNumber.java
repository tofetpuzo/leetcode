public class missingNumber {

    public static void main(String[] args) {
        // int [] intArray = {1, 2, 3, 4, 5, 6, 7, 9, 10};
        int [] intArray  = {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13};
        missingNumbers(intArray);
    }
    public static void missingNumbers(int [] intArray) {
        int missingNumber = intArray.length+1;
        System.out.println(missingNumber);
        int m = 0;
        for (int i = 0; i < intArray.length ; i++) { 
            m = missingNumber + (i - intArray[i]);      
            System.out.println(missingNumber + "si:" + i + " "+ "s: " + intArray[i] + ""); 
        }
        System.out.println(m);              
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
