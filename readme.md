quick guide:
Requirements:
python v3.11.0
allure v2.22.0

to start tests in comandline mode run following comands:
python -m pytest tests/ 

to start tests and generate allure reports run:
python -m pytest --alluredir=tests_results/ tests/  

to see allure reports run:
allure serve tests_results/  


<img width="822" alt="Screenshot 2023-07-07 at 11 08 11" src="https://github.com/Leonova-i/Test_tasks_API/assets/114931033/751017c8-3dd2-405e-a32b-c8da27da548c">
u can see 17 tests whih included 9 private tests:
