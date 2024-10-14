<div align="center">
    <img width="400" alt="image" src="https://github.com/user-attachments/assets/1e5cdb15-340a-46cb-8223-787ef2fdf52c">
  <h1>Jungle Oneline</h1>
  <h2>키워드 중심 동료 피드백 공유 사이트</h2>
  <h4>🗝️ KeyWords <h4/>
  <p>  #RESTAPI #MongoDB #Flask #Blueprint #JWT #AWS EC2 </p>
  <br>
  <div align="center">
    <img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white"/>
    <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white"/>
    <img src="https://img.shields.io/badge/AWS%20EC2-FF9900?style=flat-square&logo=amazon-aws&logoColor=white"/>
    <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black"/>
  </div>
  <br>
</div>

---

# 개요
- 팀원 간 키워드 중심의 피드백을 공유하는 웹사이트 개발 프로젝트입니다.   
- 해커톤 형식으로, 처음 보는 동료들과 4일 내 웹 사이트 MVP 개발 및 배포를 목표로 하였으며, 프로젝트 개발 역량과 협업 능력 증진을 목적으로 진행했습니다.

# 담당 인원 및 기한
- 3박 4일
- 총 3명 (B.E 2명, F.E 1명)

# 목적
- 핵심 기능 중심의 REST API 구현 및 배포
- 압축적인 스프린트룰을 통해 빠른 개발 사이클 경험

# 사용 언어 및 프레임워크
- Flask, MongoDB, JWT, AWS EC2 (Ubuntu Linux)

# 담당 업무 및 성과 (백엔드 70%, 주관적 수치)
- **핵심 기능 REST API 구현**: 키워드, 한 줄 평 등 주요 기능을 REST API로 설계 및 구현 
- **JWT 활용 로그인/검증 시스템 구축**: 인증 및 인가 기능 구현
- **코드 리팩토링**: Blueprint 라이브러리를 활용하여 코드 가독성 개선 및 유지보수 용이성 확보 (300줄 → 100줄)
- **AWS EC2 배포**: Linux 기반 EC2 인스턴스에 웹 서비스 배포 및 운영
- **스프린트 룰 활용**: 압축적인 스프린트 개발을 통한 효율적인 개발 사이클 경험

# 아키텍처

![image](https://github.com/user-attachments/assets/5015baca-a135-47d7-8ab8-8873db42cfd5)

# 주요 기능
## Main 페이지에서 목록 보기 및 blur 기능
<img width="600" alt="image" src="https://github.com/user-attachments/assets/0201d900-a168-4ff3-b98a-d2904b27a38b">

- 유저는 로그인을 통해 Main Page에서 등록된 사용자들의 키워드가 보이는 목록을 보게됩니다.
- 해당 사용자에 대한 자신의 의견을 작성하기 전에는 blur 처리됩니다.
- 사용자를 클릭하여, 해당 사용자 상세 페이지로 이동하게 됩니다.

## 의견 제출 기능(한 줄 평, 키워드)
<img width="600" alt="image" src="https://github.com/user-attachments/assets/12e3bc57-4209-4190-859e-721b9c03c7ff">

- 상세 페이지에서 해당 사용자의 성격 키워드를 내림차순/색상 농도를 통해 파악할 수 있으며, 다른 유저들이 해당 사용자에게 남긴 한 줄 평을 볼 수 있습니다.
- 의견 제출 페이지를 통해 Good 키워드와 Bad 키워드를 선택하고 한 줄 평을 작성할 수 있습니다. (동료 한 명당 1회에 한해 작성)
- Bad 키워드는 최상위 1개만 노출됩니다.


# 엔지니어링 경험

<details>
<summary>1. Object_Id 조회 문제 해결</summary>

- **상황**: MongoDB에서 데이터를 조회할 때 기본 키인 `Object_Id`로 데이터를 찾지 못하는 문제가 발생
- **진단**: Flask가 BSON 타입을 지원하지 않아서 `Object_Id`로 데이터를 조회하지 못함
- **해결 방안**:
  1. `JSONify()`를 통해 Object_Id 문자열을 직렬화
       
        <img width="473" alt="image" src="https://github.com/user-attachments/assets/cc9ecd8b-6fcf-4e90-ab46-34bba3e41e65">

  2. BSON 타입 지원 라이브러리를 별도 import하여 처리
       
       <img width="473" alt="image" src="https://github.com/user-attachments/assets/a83a9a4a-e1cf-4567-acb8-1f7fe8ad784d">

- **결과**: Flask에서 MongoDB의 BSON 타입 Object_Id를 정상적으로 조회하고 활용할 수 있게 됨
</details>

   

<details>
<summary>2. app.py 가독성 문제 해결</summary>

- **상황**: `app.py` 파일에 `@app.route` 데코레이터가 과도하게 많아져 코드 가독성이 떨어지고 개발 생산성이 저하됨
- **진단**: `app.py`에 몰린 라우팅 로직을 분산하거나 구조 개선 필요
- **해결 방안**: Blueprint 라이브러리를 사용하여 각 기능별 모듈화
  - 기존의 `@app.route`로 정의된 라우터를 각각의 Blueprint 모듈로 이동
  - `app.py`에서 각 모듈을 등록하여 독립적인 라우팅 구조로 변경
- **결과**: 코드 길이가 300줄에서 100줄로 감소, 코드 가독성 및 유지보수성 향상
  
    ![image](https://github.com/user-attachments/assets/125b6fec-adad-463a-8ed8-2a98e7fcf519)

</details>
