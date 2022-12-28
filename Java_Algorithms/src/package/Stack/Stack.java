package Stack;

public class Stack {
    int[] arr;
    int top;
    public Stack(int size){
        this.arr = new int[size];
        this.top = -1;
        System.out.println("stack created");
    }
    public boolean isEmpty(){
        if(top == -1){
            return true;
        }else return false;
    }
    public boolean isFull() {
        if(top == arr.length -1){
            System.out.println("is full");
            return true;
        }else return false;
        
    }
    
}
