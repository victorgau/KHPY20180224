# 載入 os 模組
import os

# 主函式慣例上會被命名為 main()，程式區塊的定義是以縮排來表示。需特別注意在 python 中，縮排是有意義的。
def main():
    # 字串可以用單引號或雙引號來表示，print() 預設會自動加上換行字元
    print('Hello world!')

    # 如果字串中有用到單引號，則可以用雙引號來括住字串
    print("This is Alice's greeting.")
    # 或者使用反斜線(\)來跳脫單引號
    print('This is Bob\' greeting.')
 
    # 函式呼叫
    foo(5, 10)

    # 要重複字串，可以使用乘號 (*)
    print('=' * 10)

    # 要串接自創，可以使用加號 (+)
    print('Current directory is ' + os.getcwd() )

    # 變數開始使用前，要給定初值
    counter = 0
    counter += 1

    # 串列裡頭的元素可以有不同的資料型態
    food = ['apples', 'oranges', 'cats']

    # for 迴圈的寫法如下，會依序從串列中取出元素來執行
    for i in food:
        print('I like to eat' + i)

    # range() 函式的輸出可被視為 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 的串列
    print('Count to ten:')
    for i in range(10):
        print(i)

# 函式定義，最後記得要有冒號
def foo(param1, secondParam):
    res = param1 + secondParam

    # 字串的插入方式，如果底下所示。
    print("{0} plus {1} is equal to {2}".format(param1, secondParam, res))

    # if 條件式如下，後面要有一個冒號，表示程式區塊的開始。
    # 在 python 中使用 and 跟 or 做為邏輯運算子，增加程式的可讀性。
    if res < 50:
        print('foo')
    elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):
        print('bar')
    else:
        print('moo')

    return res # 單行的註解，使用井字號
    ''' 多行的註解，
    可以使用三個單引號或雙引號，
    多行的字串也是這樣使用。'''

# 當程式直接被執行時，__name__ 變數會被設成 '__main__'，條件式內的程式區塊會被執行。
# 這一段程式碼寫在最後的另一個原因是為了讓所有的 def 定義在 main() 被執行前都已被讀入。
if __name__=='__main__':
    main()
