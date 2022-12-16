
'''You are given an integer array prices where prices[i] is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i]. Otherwise, you will not receive any discount at all.

Return an integer array answer where answer[i] is the final price you will pay for the ith item of the shop, considering the special discount.'''


# prices = [8,4,6,2,3]
prices = [1,2,3,4,5]
# prices=[10,1,1,6]
n=len(prices) 
ans=[]
for i in range(n):
    cp=prices[i] 
    for disc in prices[i+1:]:
        if disc<=cp:
            diff=cp-disc 
            ans.append(diff)
            break
    else:
        ans.append(cp)
print(ans)

