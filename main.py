#write to check if a person is buying oranges at $10 and later selling it at $12. Find if he has profit and loss.
costprice=int(input("Enter the cost price: "))
sellingprice=int(input("Enter the selling price: "))
if costprice<sellingprice:
    profit=sellingprice-costprice
    print("Total profit:",profit)
else:
    loss=costprice-sellingprice
    print("Total loss:",loss)