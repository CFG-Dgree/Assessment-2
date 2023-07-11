# Section 1: Theory Questions [31 marks]

## 1.1    What does SDLC stand for?	1 mark
    Software development life cycle

## 1.2   What exception is thrown when you divide a number by 0?	1 mark
    ArithmeticException
## 1.3   What is the git command that moves code from the local repository to the remote repository? 	1 mark
    git push
## 1.4   What does NULL represent in a database? 	   1 mark
    absence of data

## 1.5   Name 2 responsibilities of the Scrum Master 	2 marks

## 1.6   Name 2 debugging methods, and when you would use them.	  4 marks
    exception handling ; Testing
## 1.7   Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need. 

def can_pay(price, cash_given):
   if cash_given >= price:
       return True
   else:
       return False
	  5 marks

This function will throw TypeError once the input are not numeric values.
I will add a try/except statement in a while loop for, which could give reminder and repetitive request to user when the type input is not numeric.


## 1.8    What is git branching? Explain how it is used in Git. 	  6 marks
Git branching is a feature in Git that allows developers to create separate lines of development, which could be merged into the main with request.

## 1.9  Design a restaurant ordering system. 
           You do not need to write code, but describe a high-level approach: 
a.Draw a list of key requirements:
b.What are your main considerations and problems?
c.What components or tools would you potentially use? 
	  10 marks
### key requirements:
1. Menu presentation
2. Payment system
3. Order placement linked with merchant end.
4. Table track
### Challenges:
1. Accessibility for everyone (people don't use smart phone or with disability)
2. UI/UX
3. Payment security
### Tools:
1. Backend algorithm (Python, Java)
2. Frontend interface design (html/css/JavaScript)
3. API for payment.