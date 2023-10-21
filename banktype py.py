amount=eval(input("ENTER THE AMOUNT YOU WANT TO WITHDRAW="))
amount=amount-100

twok=amount//2000
amount=amount%2000

oneh=amount//100
amount=amount%100

fiveh=amount//500
amount=amount%500

print("NUMBER OF TWO THOUSAND RUPEE NOTE=",twok)
print("NUMBER OF FIVE HUNDRED RUPEE NOTE=",fiveh)
print("NUMBER OF ONE HUNDRED RUPEE NOTE=",oneh+1)
