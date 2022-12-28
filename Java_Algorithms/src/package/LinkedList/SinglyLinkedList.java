package LinkedList;

public class SinglyLinkedList {
    public Node head;
    public Node tail;
    public int size;

    public Node createSingLNode(int nodeValue){
        // create new node before assignning them
        head = new Node();
        Node node = new Node();
        node.next = null;
        node.value = nodeValue;
        head = node;
        tail = node;
        size = 1;
        return head;
              
    }
    // Insert Node in the sL
    public void insertLinkedList(int nodeValue, int location) {
        Node node = new Node();
        node.value = nodeValue;
        if (head == null){
            node = createSingLNode(nodeValue);
            return;
        } else if(location == 0){
            node.next = head;
            head = node;           
        } else if(location >= size){
            node.next = null;
            
        }
        

        
    }
} 
