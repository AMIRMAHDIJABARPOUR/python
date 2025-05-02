# محاسبه مجموع اعداد زوج
status = False
while not status:
    number = int(input("enter your Number: "))
    if number < 1:
        print("enter a larger number")
    else:
        total = 0
        for num in range(1, number + 1):
            if num % 2 == 0:
                total += num
        print(f"Sum of even numbers: {total}")
        status = True


# توضیح: برنامه‌ای بنویسید که از کاربر یه عدد بگیره و مجموع اعداد زوج از 1 تا اون عدد رو حساب کنه.



# مفاهیم: حلقه‌ها، شرط‌ها، عملیات ریاضی.



# چاپ الگوی ستاره





# توضیح: برنامه‌ای بنویسید که یه عدد از کاربر بگیره و یه الگوی مثلثی از ستاره‌ها چاپ کنه (مثلاً با 3: *، **، ***).

Number_of_stars = int (input("Enter Number of stars you want to see in triangel form :"))
for num in range(Number_of_stars):
    star=""
    for i in range (num):
        star+="*"
    print(star)


# مفاهیم: حلقه‌ها، رشته‌ها.



# حدس عدد تصادفی





# توضیح: برنامه‌ای بنویسید که یه عدد تصادفی بین 1 تا 100 تولید کنه و کاربر باید حدس بزنه (با راهنمایی "بزرگ‌تر" یا "کوچک‌تر").
import random 
True_Number= random.randint(1,100)
while True:
    guess=int(input("Enter your guess:"))
    if guess==True_Number:
        status=True
        print ("congratulation you guess right")
        break
    elif True_Number>guess:
        print ("you guess a lower number")
    else:
        print ("you guess a bigger number ")

# مفاهیم: حلقه‌ها، شرط‌ها، ماژول random.



# محاسبه تعداد ارقام عدد
Num= str(input ("Enter your Number:"))
print(len(Num))



# توضیح: برنامه‌ای بنویسید که یه عدد از کاربر بگیره و بگه چند رقم داره.



# مفاهیم: حلقه‌ها، عملیات ریاضی یا تبدیل به رشته.



# چک کردن حروف بزرگ و کوچک
word=str(input("please enter your word:"))
def info (word):
    numbers="0123456789"
    Num,Cap,small=0,0,0
    for s in word:
        if s in numbers:
            Num+=1
        elif s == s.upper() and s != " ":
            Cap+=1
        elif s == s.lower():
            small+=1
    return Num,Cap,small
Num,Cap,small = info(word)
print("you entered %i capital words and %i small words and %i Numbers"%(Cap,small,Num))



# توضیح: تابعی بنویسید که یه رشته بگیره و تعداد حروف بزرگ و کوچکش رو بشماره.



# مفاهیم: رشته‌ها، حلقه‌ها، شرط‌ها.



# جمع عناصر لیست





# توضیح: برنامه‌ای بنویسید که یه لیست از اعداد رو از کاربر بگیره و مجموعشون رو حساب کنه.
Total=0
def check (number):
    true_numbers="0123456789"
    for i in number:
        if number not in true_numbers:
            return False
            
    return True
while True:
    num=input("please Enter a Number :")
    if num == "stop":
        print ("ok ! your Total is %i:"%(Total))
        break
    elif check(num) !=True:
        print ("please do not use the alphabet or anything exept numbers")
        continue
    else:
        Total+=int(num)


# مفاهیم: لیست‌ها، حلقه‌ها.



# پیدا کردن بزرگ‌ترین عدد





# توضیح: برنامه‌ای بنویسید که از کاربر 5 عدد بگیره و بزرگ‌ترینشون رو چاپ کنه.
largest=0
for i in range (5):
    num = int(input ("input Enter your number :"))
    if num>largest:
        largest=num
print ("the bigger number in yout number entered is %i "%(largest))

# مفاهیم: شرط‌ها، حلقه‌ها، متغیرها.



# تبدیل عدد به باینری
# ترجیه دادم که از تابع تبدیل به باینری استفاده نکنم و برای اینکه قوی تر بشم خودم یه تابع بنویسم که این کار رو انجام بده 
bi=""
num=int (input ("please enter your number :"))
def check (number):
    true_numbers="0123456789"
    for i in number:
        if number not in true_numbers:
            return False
            
    return True

while True:

    if num/2<1:
        bi=str(int(num%2))+bi
        break
    else:
        bi=str(int(num%2))+bi
        num/=2
    

print("the binary form of your number is "+bi)


# توضیح: تابعی بنویسید که یه عدد بگیره و معادل باینریش رو (به صورت رشته) برگردونه.



# مفاهیم: حلقه‌ها، عملیات ریاضی، رشته‌ها.



# حذف کاراکترهای تکراری





# توضیح: برنامه‌ای بنویسید که یه رشته از کاربر بگیره و کاراکترهای تکراریش رو حذف کنه (مثلاً "hello" بشه "helo").
word=str(input("please enter your word:"))
alpha=[]
new_word=""
for i in word:
    if i in alpha:
        continue
    else:
        alpha.append(i)
        new_word+=i
print(new_word)

# مفاهیم: رشته‌ها، حلقه‌ها، لیست‌ها.



# محاسبه توان عدد
def  power( num, power):
    for i in range (int(power)):
        num*=num





# توضیح: تابعی بنویسید که یه عدد و توانش رو از کاربر بگیره و نتیجه رو بدون استفاده از عملگر ** حساب کنه.



# مفاهیم: حلقه‌ها، توابع، عملیات ریاضی.