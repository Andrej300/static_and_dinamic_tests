### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # == instead of =
      return True
    else  #missing colon
      return False
   

  dif highest_card(self, card1 card2): # the right word "def", instead of "dif". Missing comma after caard1.
  if card1.value > card2.value: #Wrong indentation
    return card #Wrong indentation  # 'card1' instead of 'card'
  else: #Wrong indentation
    return card2 #Wrong indentation
  


def cards_total(self, cards):
  total  # 'total' variable is not assigned to anything
  for card in cards:
    total += card.value
    return "You have a total of" + total  # wrong syntax, should be: f"You have a total of {total}"
  
```
