# Django-SQL-sample

# install
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -r requirements-test.txt
pip install -r requirements-travisci.txt
```

# create database
```
python manage.py makemigrations
python manage.py migrate
```

# start server
```
python manage.py runserver 0.0.0.0:8000
```

# Unit Test
```
# 运行项目中所有APP的单元测试
python manage.py test
# 运行app1下的单元测试
python manage.py test app1
# 运行app1下的A1TestCase用例
python manage.py test app1.A1TestCase
# 同上了类推
python manage.py test app1.A1TestCase.mehthod1

# 执行目录下所有的测试(所有的test*.py文件)：
python manage.py test
# 执行animals项目下tests包里的测试：
python manage.py test animals.tests
# 执行animals项目里的test测试：
python manage.py test animals
# 单独执行某个test case：
python manage.py test animals.tests.AnimalTestCase
# 单独执行某个测试方法：
python manage.py test animals.tests.AnimalTestCase.test_animals_can_speak
# 为测试文件提供路径：
python manage.py test animals/
# 通配测试文件名：
python manage.py test --pattern="tests_*.py"
# 启用warnings提醒：
python -Wall manage.py test
```

# LiveServerTestCase
```
# Changed in Django 1.9:
# In earlier versions, the live server’s default address was always 'localhost:8081'.
python manage.py test --liveserver=localhost:8081
python manage.py test --liveserver=localhost:8082

python manage.py test --liveserver=localhost:8082,8090-8100,9000-9200,7041

python manage.py test apps.live_server_test.selenium.MySeleniumTests.test_login
```

# Coverage
```
coverage run --source='.' manage.py test apps
coverage report
```