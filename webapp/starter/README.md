## Project base

프로젝트 생성을 쉽게 해주기 위한 directory

사용시 git clone 후`projectname`만 해당 프로젝트명으로 변경해서 사용
- `env.example` 파일을 `.env`로 변환 후 `projectname` 변경
- `.env` 파일에 필요한 정보(postgres 등) 넣기 

```
# pyenv, autoenv 사용시 자동 activate
pyenv activate projectname

# local, production 환경별로 settings module 지정.
# 지정하지 않으면 `--settings=`로 직접 입력 가능.
DJANGO_SETTINGS_MODULE='projectname.settings.local'

# secret key, psql 정보 입력
POSTGRES_DB_NAME=''
DJANGO_SECRET_KEY=''
POSTGRES_USER=''
POSTGRES_PASSWORD=''
DJANGO_ALLOWED_HOSTS=['*']

# 나머지 세팅들은 필요할 때 사용

# AWS Settings
# DJANGO_AWS_ACCESS_KEY_ID=
# DJANGO_AWS_SECRET_ACCESS_KEY=
# DJANGO_AWS_STORAGE_BUCKET_NAME=

# DJANGO_ADMIN_URL=
```

> django secret key 생성법
> [django secret key generator](http://www.miniwebtool.com/django-secret-key-generator/)에 들어가서 새로운 secret key를 generate 한 후 env에 넣어준다.


- database settings: 현재는 local db가 sqlite. 맞는 psql 세팅으로 변경한 후 진행 가능
