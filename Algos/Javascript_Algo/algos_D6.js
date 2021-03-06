/* 
    Two challenges!

    addToFront: Write a method of the SLList class that accepts a value, and adds a node with that 
    value to the front of the list. 
    
    Steps:
        1. Create a new node
        2. Assign that node's next attribute to the list's current head
        3. Assign the list's current head to the new node

    KEEP IN MIND: What dictates that a node is the first element in the list? Might need to reset that.

    addToBack: Write a method of the SLList class that accepts a value, and adds a node with that
    value to the BACK of the list.

    Steps:
        1. Create a new node
        2. Start at the head of the list
        3. Run to the last node
        4. Set the last node's next attribute to the new node
    EDGE CASE: What if the list is empty? How do we even know if the list is empty?


    BONUS IF YOU ARE DONE QUICKLY:
    contains: Write a method of the SLList class that accepts a value, and returns a boolean based
    on whether or not a node with that value exists in the list

    Steps:
        1. Start at the head of the list
        2. Check if the value of the node we're looking at equals the value passed in
        3. If it does, return true
        4. If not, go to the next node.
        5. If we checked every single node and we're still running the method, the value does not exist in the list.
*/

// https://www.youtube.com/watch?v=ZBdE8DElQQU

class SLNode {
    constructor(value) {
        this.value = value;
        this.next = null; // Why??
        
    }
}

class SLList {
    constructor(){
        this.head = null;
    }

    addToFront(value) {
        
        return this;
    }

    addToBack(value) {
        return this;
    }

    contains(value) {
    }
}



var newList = new SLList(); // instance

newList.addToBack(5).addToBack(1).addToFront(3); // calling methods


// BONUS CASES
// var contains5 = newList.contains(5);
// var contains5Expected = true;
// console.log(contains5 == contains5Expected);

// var contains2 = newList.contains(2);
// var contains2Expected = false;
// console.log(contains2 == contains2Expected);

// var contains3 = newList.contains(3);
// var contains3Expected = true;
// console.log(contains3 == contains3Expected);