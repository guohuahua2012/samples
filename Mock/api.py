from flask import Flask,jsonify,request
import sqlite3

# 定义请求方式错误
method_err = {
    "code": 301,
    "msg": "请求方式不正确，只支持POST请求"
}

# 参数错误
param_err = {
    "code": 302,
    "msg": "请求参数错误，请检查入参"
}

# 余额不足
money_err = {
    "code": 303,
    "msg": "账户余额不足"
}

# 价格错误
price_err = {
    "code": 304,
    "msg": "价格不合法"
}

# 用户不存在
user_err = {
    "code":305,
    "msg": "该用户不存在"
}

# 成功的信息
success_msg = {
    "code":200,
    "msg": "支付成功"
}

# 数据库异常
db_err = {
    "code":306,
    "msg": "数据库错误"
}

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

def check_float(string):
    str1 = str(string)
    if str1.count('.') > 1: #判断小数点是否大于1
        return False
    elif str1.count('-') > 0:
        return False
    elif str1.isdigit():
        return False
    else:
        new_str = str1.split('.') # 按小数点分割字符
        frist_num = new_str[0] # 取分割完之后这个list的第一个元素
        if frist_num.isdigit() and new_str[1].isdigit():
            # 如果小数点两边都是整数的话，那么就是一个小数
            return True
        else:
            return False

def op_db(sql):
    db = sqlite3.connect(r'D:/SQLdb/main.db') # 指定数据库
    course = db.cursor() # 创建游标
    try: # 捕捉异常,如果有sql写的不对就返回异常
        course.execute(sql) # 执行sql
    except sqlite3.Error as e:
        # 出异常了，则抛出异常信息
        return False
    else:
        res = course.fetchone() # 获取查询结果
        db.commit()
        return True # 返回数据
    finally:
        # 不管出没出异常都关闭数据库
        course.close() # 关闭游标
        db.rollback() # 回滚
        db.close()

def  check_balance(user_id, price):
    select_sql = 'select money from accounts where user_id = %s;' %user_id
    data = op_db(select_sql) # 获取sql执行的结果
    if data: # 如果返回的数据不为空
        if not data: #not就是取反的意思，如果返回False的话，就是真了，就说明出错了，返回数据库错误
            return db_err
        else: # 如果select有结果的话，就获取到这个用户的账号信息
            money = data[0] # 数据库获取到的结果是一个元组，就一个元素就是价格
            if money > price: # 如果账户余额大于等于价格的话，修改价格
                target_money = money - price
                # 更新余额的sql
                update_sql = 'update accounts set money = %s where user_id = %s;' %(target_money,user_id)
                op_db(update_sql)
            else: # 如果余额不足的话，返回余额错误信息
                return money_err
    else: #如果数据是空，就是用户信息获取不到
        return user_err


@app.route('/pay/',methods=['POST'])
def pay():
    # def pay() 就是定义一个函数，这个函数写的就是接口业务的逻辑
    if request.method != 'POST': # 如果不是post请求的话，返回请求类型错误
        return jsonify(method_err) # return 就返回数据了，jsonify就是把python里面的数据类型（字典、list）转成json串

    else:
        user_id = request.values.get('user_id') # 使用request.values.get获取到传入的参数，user_id
        price = request.values.get('price') # 获取到支付的价格

        if user_id and price: # 判断两个入参是否都传了，user_id和price
            if price.isdigit(): # 如果价格是整数的话
                price = int(price) # 接收过来的入参是字符串类型的，所以要转成int类型的，才可以加减
            elif check_float(price): # 这里调用了一个函数，在上面定义了，是校验传入的价格是不是小数的
                price = float(price)
            else: # 如果不是整数也不是小数，返回价格错误
                return jsonify(param_err)

        # 上面都校验通过之后，数据就是合法的，就得扣钱了，那就是操作数据库
        # 再写一个函数专门用来扣钱
            res = check_balance(user_id, price)  # 调用检查余额函数

            return jsonify(res)
        else: #如果user_id或者price获取不到的话，返回参数错误
            return jsonify(param_err)

if __name__ == '__main__':
    app.run(debug=True) # 运行程序，debug的意思是调试模式运行，可以看到请求，默认端口号是5000，可以使用port参数指定端口号











