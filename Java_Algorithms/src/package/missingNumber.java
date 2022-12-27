public class missingNumber {

    public static void main(String[] args) {
        int [] intArray = {1, 2, 3, 4, 5, 6, 8, 9, 10};
        System.out.println(missingNumbers(intArray));
    }
    public static int missingNumbers(int [] intArray) {
        int missingNumber = 0;
        for (int i = 1; i < intArray.length; i++) {
            for (int j = intArray.length - 1; j >= i; j--) {
                missingNumber = (missingNumber += (j / i)) % 10;
            }
            
        }
        return missingNumber;
        
    }
    
}
