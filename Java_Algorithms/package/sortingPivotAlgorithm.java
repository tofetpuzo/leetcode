

public class sortingPivotAlgorithm{

   public static void main(String[] args) {
    System.out.println(sumDigits(45));
    System.out.println(GCD(48, 18));
    System.out.println(convertDecimalToBinary(8));
      

   }
   public static int sumDigits(int n) {
      if (n == 0 || n < 0) {return 0;}
      return n + sumDigits(n - 1);
   }

   public static int GCD(int a , int b) {
      if (b == 0 || (a < 0 || b < 0)) {return a;}
      return GCD(b , a % b);
      
   }
   public static int convertDecimalToBinary(int n) {
      if (n == 0 || n < 0) {return 0;}
      return n%2 + 10 * convertDecimalToBinary(n/2);
   }

}
