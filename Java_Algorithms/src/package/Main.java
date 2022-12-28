import LinkedList.SinglyLinkedList;

public class Main {
    public static void main(String[] args) {
        SinglyLinkedList sl = new SinglyLinkedList();
        sl.createSingLNode(5);
        System.out.println(sl.head.value);
    }
}
