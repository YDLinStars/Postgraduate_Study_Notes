import smtplib
from email.mime.text import MIMEText
from email.header import Header

def email(csdn_article_title,csdn_article_url):

    sender = '913397230@qq.com'#填写发件人
    pwd = 'wlphpcnmjpcvbbfi'#登录密码
    receivers = ['yongdonglin@126.com']#填写收件人

    mainText="网站有内容更新,更新题目为："+csdn_article_title+"更新网址为："+csdn_article_url
    message = MIMEText(mainText,"plain",'utf-8')
    # 三个参数：第一个为文本内容，第二个为plain设置文本格式，第三个为utf-8设置编码
    message ['From'] = "小道消息 <913397230@qq.com>"
    message ['To'] = "小林子 <yongdonglin@126.com>"

    subject = "CSDN网站有内容更新"
    #邮件主题
    message["Subject"] = subject

    try:
        # 使用非本地服务器，需要建立ssl连接
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com",465)
        #发件箱邮件服务器
        smtpObj.login(sender,pwd)
        smtpObj.sendmail(sender,receivers,message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error：无法发送邮件.Case:%s"%e)