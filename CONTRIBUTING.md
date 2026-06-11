# 프로젝트 개발 가이드

## 개발 환경

### Python 버전

본 프로젝트는 아래 버전을 기준으로 개발합니다.

```bash
Python 3.10
```

버전 확인:

```bash
python --version
```

---

# 초기 세팅 방법

## 1. 프로젝트 클론

```bash
git clone <repository-url>
cd <project-name>
```

---

## 2. 가상환경(venv) 생성

Mac / Linux:

```bash
python3.10 -m venv venv
```

Windows:

```bash
py -3.10 -m venv venv
```

---

## 3. 가상환경 활성화

Mac / Linux:

```bash
source venv/bin/activate
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

활성화 성공 시 터미널 앞에 `(venv)` 표시가 나타납니다.

---

## 4. 패키지 설치

```bash
pip install -r requirements.txt
```

---

# 패키지(requirements) 관리 규칙

## 새로운 패키지를 설치한 경우

```bash
pip install fastapi
pip freeze > requirements.txt
```

그 후 GitHub에 함께 커밋합니다.

---

# Git 브랜치 규칙

## 브랜치 구조

```text
main      : 최종 배포 브랜치
develop   : 통합 개발 브랜치
feature/* : 개인 작업 브랜치
```

예시:

```bash
git checkout -b feature/login-api
```

---

# 작업 규칙

* main 브랜치 직접 push 금지
* 반드시 feature 브랜치에서 작업
* 작업 완료 후 Pull Request(PR) 생성
* 작업 시작 전 최신 코드 pull 받기

```bash
git pull origin develop
```

---

# 업로드 금지 파일

```text
venv/
node_modules/
.env
__pycache__/
```

특히 아래 정보는 절대 업로드 금지:

* API KEY
* 비밀번호
* 개인 환경설정 파일
* 인증서 파일

---

# 환경 변수(.env)

각자 `.env` 파일을 생성해서 사용합니다.

```env
OPENAI_API_KEY=
MONGO_URI=
JWT_SECRET=
```

---

# 권장 작업 순서

```text
1. 최신 코드 pull
2. feature 브랜치 생성
3. 기능 개발
4. commit
5. push
6. Pull Request 생성
```

---

# Commit 메시지 규칙

```text
feat: 로그인 기능 추가
fix: 토큰 오류 수정
refactor: 챗봇 로직 개선
docs: README 수정
```

---

# 문제 발생 시

## 패키지 오류 발생

```bash
pip install -r requirements.txt
```

## venv 활성화가 안 된 경우

터미널 앞에 `(venv)` 표시가 있는지 확인 후 다시 활성화합니다.

---

# 팀 협업 규칙

아래 사항 변경 시 팀원들과 반드시 공유해주세요.

* 새로운 패키지 설치
* API 구조 변경
* 환경 변수 추가
* DB 구조 변경
* requirements.txt 변경
