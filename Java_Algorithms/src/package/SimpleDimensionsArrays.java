

public class SimpleDimensionsArrays {
    public int[] arr;
    public SimpleDimensionsArrays(int sizes) {
        arr = new int[sizes];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.MIN_VALUE;
        }       
    }
    public static void main(String[] args) {
        SimpleDimensionsArrays sda = new SimpleDimensionsArrays(10);
        sda.insert(1, 4);


    }
   

    public void insert(int location, int valueToBeInserted) {

        try {
            if (arr[location] == Integer.MIN_VALUE ){
                arr[location] = valueToBeInserted;
                System.out.println("success");
            }else{
                System.out.println("this cell is success");
            }
            
        } catch (ArrayIndexOutOfBoundsException e) {
            // TODO: handle exception
            System.out.println("this cell is success");
        }

    }
}
