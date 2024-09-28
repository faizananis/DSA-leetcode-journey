class MyCircularDeque {
public:
    ListNode* head=NULL;
    int maxSize=0;
    int size=0;
    MyCircularDeque(int k) {
        maxSize=k;
        head=new ListNode(-1);
    }
    bool insertFront(int value) {
        if(size==maxSize)
        {
            return false;
        }
        ListNode* node= new ListNode(value);
        node->next=head->next;
        head->next=node;
        size++;
        return true;
    }
    bool insertLast(int value) {
        if(size==maxSize)
        {
            return false;
        }
        ListNode* node=new ListNode(value);
        ListNode* temp=head;
        while(temp->next)
        {
            temp=temp->next;
        }
        temp->next=node;
        size++;
        return true;
    }
    bool deleteFront() {
        if(size==0)
        {
            return false;
        }
        ListNode* temp=head->next;
        head->next=head->next->next;
        temp->next=NULL;
        delete temp;
        size--;
        return true;
    }
    bool deleteLast() {
        if(size==0)
        {
            return false;
        }
        ListNode* trav=head;
        ListNode* temp=NULL;
        while(trav->next->next)
        {
            trav=trav->next;
        }
        temp=trav->next;
        trav->next=NULL;
        delete temp;
        size--;
        return true;
    }
    int getFront() {
        if(size==0)
        {
            return -1;
        }
        return head->next->val;
    }
    int getRear() {
        if(size==0)
        {
            return -1;
        }
        ListNode* temp=head->next;
        while(temp->next)
        {
            temp=temp->next;
        }
        return temp->val;
    }
    bool isEmpty() {
        return size==0;
    }
    bool isFull() {
       return size==maxSize;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */