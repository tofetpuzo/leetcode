package LinkedList;

public class SinglyLinkedList {
    public Node head;
    public Node tail;
    public int size;

    public Node createSingLNode(int nodeValue) {
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
        if (head == null) {
            node = createSingLNode(nodeValue);
            return;
        } else if (location == 0) {
            node.next = head;
            head = node;
        } else if (location >= size) {
            node.next = null;
            tail.next = node;
            tail = node;
        } else {
            Node tNode = head;
            int index = 0;
            while (index < location - 1) {
                tNode = tNode.next;
                index++;
            }
            Node nextNode = tNode.next;
            tNode.next = node;
            node.next = nextNode;
        }
        size += 1;

    }

    // Traverse method of SL
    public void traverseSinglyLinkedList() {

        if (head == null) {
            System.out.println("this sl does not exist");
        } else {
            Node tempNode = head;
            for (int i = 0; i < size; i++) {
                System.out.print(tempNode.value);
                if (i != size - 1) {
                    System.out.print("->");
                }
                tempNode = tempNode.next;
            }
        }
        System.out.println("\n");
    }

    // search method of SL
    public boolean searchSinglyLinkedList(int searchNode) {

        if (head == null) {
            System.out.println("this sl does not exist");
        } else {
            Node tempNode = head;
            for (int i = 0; i < size; i++) {

                if (tempNode.value == searchNode) { 
                    System.out.print("tthis is the index which it was found:" + "  " + " + "+ i +" in this index");
                    return true;
                }
                tempNode = tempNode.next;
            }
        }
        System.out.println("node not found");
        return false;   
        
    }
    // delete a node
    public boolean deleteSinglyLinkedList(int deleteNode) {

        if (head == null) {
            System.out.println("this sl does not exist");

        } 
        else {
            Node tempNode = head.next;
            Node prevNode = head;
            for (int i = 0; i < size; i++) {
                if (tempNode.value == deleteNode) {
                    prevNode.next = tempNode.next; 
                    tempNode = tempNode.next = null;
                    break;
                }
                prevNode = prevNode.next;
            }
        }
        size-=1;
        return false;   
        
    }
    
    
}
