

:: 开机自启动的设置
:: (1) win + R , 输入 taskschd.msc
:: (2) 操作/创建基本任务
:: attention 属性/常规  勾选不管用户是否登录都要运行，构选不存储密码，该任务只有访问本地计算机资源的权限
:: 具体查看我的知乎回答, https://www.zhihu.com/question/59929700/answer/2828717274

:: 这个是在 win 机器上启动 conda 环境的 bat 文件，直接双击就可以运行

:: 执行 conda 启动的 .bat, conda 启动的图标，点击查看源就能找到启动的 bat 文件的地址
call C:\ProgramData\Anaconda3\Scripts\activate.bat

python C:\Users\lingdequan\Desktop\map_depot\map_depot_for_SaturnDatabase.py --port 11103 --use_cache True

:: 暂停，否者报错就会是个黑框一散而过
pause

