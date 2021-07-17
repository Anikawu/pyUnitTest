
def forex_function(price,rate):

    price = input("輸入幣別與價錢 (EX:USD 1500): ")
    rate  = float(input("輸入匯率(EX:28.1): "))
    for num in price.split(): #以空白分割字串
        try:
           # 利用join的方式返回filter後的字串
            num = float("".join(filter(lambda d: str.isdigit(d) or d == '.', price)))
            payment = num * rate
            ans="Payment=TWD {}".format( round(payment)) #round()四捨五入到整數
            print(ans)
            return ans
        except ValueError:
             pass


'''
方法1
 a=float(num)

payment = a * rate
Ans = "Payment=TWD {}".format( round(payment)) #round()四捨五入到整數
print(Ans)
return Ans

方法2
# 利用join的方式返回filter後的字串
num = float("".join(filter(lambda d: str.isdigit(d) or d == '.', price)))
payment = num * rate
ans="Payment=TWD "+ str(round(payment)) #四捨五入到整數

join :用指定的符號來連接多個字串('(要用來隔開的符號)'.join)
因不需要符號隔開  所以為空
lambda 就是一個不用宣告的函式 d是指派給他的變數
然後去判斷  str.isdigit(d) 檢查字串中是否有數字 或是 數字中有 小數點
'''