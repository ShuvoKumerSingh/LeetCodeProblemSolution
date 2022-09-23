class RichestCustomerWealth:

    def get_maximumWealth(self,accounts):
        result_lst = 0
        for i in accounts:
            sum =0
            if i is list:
                for j in i:
                    sum+=j
                if sum>result_lst:
                    result_lst = sum
        return result_lst

ans = RichestCustomerWealth()
accounts = [[1, 2, 3], [3, 2, 1]]
print(ans.get_maximumWealth(accounts))



