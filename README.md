# test_task_xone



git clone https://github.com/AlexseyDedul/test_task_xone.git

cd test_task_xone/test_task

python3 -m venv venv

source venv/bin/activate

create .env file via .env-example and move to test_task folder

docker-compose up --build

docker-compose exec web python3 manage.py migrate
