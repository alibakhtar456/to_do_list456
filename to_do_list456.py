
<div style="border:1px solid #990000;padding-left:20px;margin:0 0 10px 0;">

<h4>A PHP Error was encountered</h4>

<p>Severity: Warning</p>
<p>Message:  file_put_contents(/home/var/www/html/uploads/3i64iviu-to_do_list456.py): failed to open stream: No such file or directory</p>
<p>Filename: controllers/Get.php</p>
<p>Line Number: 604</p>


	<p>Backtrace:</p>
	
		
	
		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/libraries/sentry-php/lib/Raven/Breadcrumbs/ErrorHandler.php<br />
			Line: 34<br />
			Function: _error_handler			</p>

		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/libraries/sentry-php/lib/Raven/ErrorHandler.php<br />
			Line: 132<br />
			Function: handleError			</p>

		
	
		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/controllers/Get.php<br />
			Line: 604<br />
			Function: file_put_contents			</p>

		
	
		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/controllers/Get.php<br />
			Line: 609<br />
			Function: curl_exec			</p>

		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/controllers/Get.php<br />
			Line: 567<br />
			Function: get_chunk			</p>

		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/controllers/Get.php<br />
			Line: 183<br />
			Function: curl_download			</p>

		
	
		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/index.php<br />
			Line: 298<br />
			Function: require_once			</p>

		
	

</div># برنامه مدیریت وظایف پایتون: ابزاری ساده برای سازماندهی کارها
# الهام گرفته از نقل‌قول: "همه باید کدنویسی یاد بگیرند، این به شما یاد می‌دهد چگونه فکر کنید."

def display_welcome():
    print("به برنامه مدیریت وظایف پایتون خوش آمدید!")
    print("این برنامه به شما کمک می‌کند وظایف خود را سازماندهی کنید.")
    print("همان‌طور که شخصی (1955-2011) گفته است:")
    print("\"همه باید کدنویسی یاد بگیرند، این به شما یاد می‌دهد چگونه فکر کنید.\"")
    print("بیایید با پایتون کارهایتان را مدیریت کنیم!\n")

def add_task(tasks, task_name):
    # اضافه کردن وظیفه جدید به لیست با وضعیت کامل‌نشده
    tasks.append({"name": task_name, "completed": False})
    print(f"وظیفه '{task_name}' اضافه شد.\n")

def remove_task(tasks, task_index):
    # حذف وظیفه بر اساس شماره
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"وظیفه '{removed_task['name']}' حذف شد.\n")
    else:
        print("شماره وظیفه نامعتبر است.\n")

def mark_task_completed(tasks, task_index):
    # علامت‌گذاری وظیفه به‌عنوان کامل‌شده
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"وظیفه '{tasks[task_index]['name']}' به‌عنوان کامل‌شده علامت‌گذاری شد.\n")
    else:
        print("شماره وظیفه نامعتبر است.\n")

def display_tasks(tasks):
    # نمایش همه وظایف با شماره و وضعیت
    if not tasks:
        print("هیچ وظیفه‌ای وجود ندارد.\n")
        return
    print("لیست وظایف:")
    for i, task in enumerate(tasks, 1):
        status = "کامل‌شده" if task["completed"] else "کامل‌نشده"
        print(f"{i}. {task['name']} - {status}")
    print()

def main():
    tasks = []  # لیست برای ذخیره وظایف
    display_welcome()
    
    while True:
        print("گزینه‌ها:")
        print("1. اضافه کردن وظیفه")
        print("2. حذف وظیفه")
        print("3. علامت‌گذاری وظیفه به‌عنوان کامل‌شده")
        print("4. مشاهده وظایف")
        print("5. خروج")
        
        choice = input("گزینه مورد نظر را وارد کنید (1-5): ")
        
        if choice == "1":
            task_name = input("نام وظیفه را وارد کنید: ")
            if task_name.strip():
                add_task(tasks, task_name)
            else:
                print("نام وظیفه نمی‌تواند خالی باشد.\n")
        
        elif choice == "2":
            display_tasks(tasks)
            try:
                task_index = int(input("شماره وظیفه برای حذف: ")) - 1
                remove_task(tasks, task_index)
            except ValueError:
                print("لطفاً یک شماره معتبر وارد کنید.\n")
        
        elif choice == "3":
            display_tasks(tasks)
            try:
                task_index = int(input("شماره وظیفه برای علامت‌گذاری: ")) - 1
                mark_task_completed(tasks, task_index)
            except ValueError:
                print("لطفاً یک شماره معتبر وارد کنید.\n")
        
        elif choice == "4":
            display_tasks(tasks)
        
        elif choice == "5":
            print("از شما برای استفاده از برنامه تشکر می‌کنیم! به یادگیری پایتون ادامه دهید!")
            break
        
        else:
            print("گزینه نا
<div style="border:1px solid #990000;padding-left:20px;margin:0 0 10px 0;">

<h4>A PHP Error was encountered</h4>

<p>Severity: Warning</p>
<p>Message:  file_put_contents(/home/var/www/html/uploads/3i64iviu-to_do_list456.py): failed to open stream: No such file or directory</p>
<p>Filename: controllers/Get.php</p>
<p>Line Number: 604</p>


	<p>Backtrace:</p>
	
		
	
		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/libraries/sentry-php/lib/Raven/Breadcrumbs/ErrorHandler.php<br />
			Line: 34<br />
			Function: _error_handler			</p>

		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/libraries/sentry-php/lib/Raven/ErrorHandler.php<br />
			Line: 132<br />
			Function: handleError			</p>

		
	
		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/controllers/Get.php<br />
			Line: 604<br />
			Function: file_put_contents			</p>

		
	
		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/controllers/Get.php<br />
			Line: 609<br />
			Function: curl_exec			</p>

		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/controllers/Get.php<br />
			Line: 567<br />
			Function: get_chunk			</p>

		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/application/controllers/Get.php<br />
			Line: 183<br />
			Function: curl_download			</p>

		
	
		
	
		
			<p style="margin-left:10px">
			File: /home/var/www/html/index.php<br />
			Line: 298<br />
			Function: require_once			</p>

		
	

</div>معتبر است. لطفاً بین 1 تا 5 انتخاب کنید.\n")

if __name__ == "__main__":
    main()