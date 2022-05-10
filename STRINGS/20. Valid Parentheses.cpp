// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
 

// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false
  
class Solution {
public:
    bool isValid(string s) {
        stack<char> t;
        int i;
        
        for(auto i:s) 
        {
            
            if(i == '(' || i =='{' || i == '[')
            {
                t.push(i);
            }
            else
            {
               
                if(t.empty() || (t.top() == '(' && i != ')') || (t.top() == '{' && i != '}') || (t.top() == '[' && i != ']'))
                {
                    return false;
                }
                
                t.pop(); 
            }
        }
        
        return t.empty();
    }
};