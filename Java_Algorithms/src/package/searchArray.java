public class searchArray {
  public static void main(String[] args) {
    int[] num = {1, 2, 3, 4, 5, 9};
    System.out.println(searchInArray(num, 2));
  }

public static int searchInArray(int[] intArray, int valueToSearch) {
      // TODO
      for (int i = 0; i < intArray.length; i++) {
        if(intArray[i] == valueToSearch) return i;
      }

    throw new IllegalArgumentException("No solution");
    
   }
}
