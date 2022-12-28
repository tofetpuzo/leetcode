import LinkedList.SinglyLinkedList;

public class Main {
    public static void main(String[] args) {
        SinglyLinkedList sl = new SinglyLinkedList();
        
        // System.out.println(sl.head.value);
        sl.createSingLNode(5);
        sl.insertLinkedList(3, 1);
        sl.insertLinkedList(45, 2);
        sl.insertLinkedList(34, 3);
        sl.insertLinkedList(11, 4);
        sl.insertLinkedList(345, 5);
        sl.traverseSinglyLinkedList();
        sl.searchSinglyLinkedList(11);
        // System.out.println(sl.head.next.value);
    }
}
