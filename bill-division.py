first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())

def bonAppetit(bill, k, b):
    annaBill = ((sum(bill)-bill[k]))/2
    if b == annaBill:
        print("Bon Appetit")
    else:
        print(int(b-annaBill))
        
bonAppetit(bill, k, b)







###********* Logic -2 ************* Working Fine ******88
"""
    count=0 
    total =0 
    bill.remove(bill[k]) 
    for i in bill: 
        count += i 
        if b==count/2: 
            print("Bon Appetit") 
        else: 
            total=int(b-(count/2)) 
    print(total)
bonAppetit(bill, k, b)
"""




###********* Logic -3 ************* Working Fine ******88
"""
def bonAppetit(bill, k, b):
  bill.pop(k)
  cost = sum(bill) / 2
  if cost == b: print("Bon Appetit")
  else: print(int(b - cost))
"""