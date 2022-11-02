## 📎 목차

1. [Service](#-service)
2. [개발 기간](#-개발-기간)
3. [개발 인원](#-개발-인원)
4. [구현 내용](#-구현-내용)
5. [기술 스택](#-기술-스택)
6. [API Endpoints](#api-endpoints)
7. [ERD](#-erd)
8. [API 명세서](#-api-명세서)

## 🚀 Service
기프티콘 구매/판매 서비스에서 웨이팅 서비스 부분만 개발

## 📆 개발 기간
- 2022.11.01 ~ 2022.11.02(2일)

## 🧑🏻‍💻 개발 인원(1명)
- 박민하

## 📝 구현 내용
1. 구매/판매 할 수 있는 기프티콘을 조회한다.
- 회원이 판매 등록한 기프티콘 수(supply)는 판매 등록 할 수 있는 기프티콘 수(demand)를 초과하지 않는다.
- **❗웨이팅 시스템 중심으로 개발하여 초과시 반환하는 error 메세지는 없다.**

2. 회원은 기프티콘을 판매할 수 있다.
- 등록가능개수(demand)를 초과한 경우에는 대기번호 부여
- 등록가능개수를 초과하지 않은 경우에는 '판매 등록 완료' 메세지 반환
- **❗웨이팅 시스템 중심으로 개발하여 회원 인증 기능은 없다.**

3. 기프티콘을 구매할 수 있다.
- 구매자가 기프티콘을 count 만큼 구매하면 supply가 구매 개수만큼 감소
- 대기번호도 구매 개수만큼 감소하고, supply가 대기번호 감소 개수만큼 증가

4. 웨이팅 정보를 조회할 수 있다.
- 대기번호가 0이 되면 삭제


## 🛠 기술 스택
Language | Framework | Database | HTTP | Tools
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> |  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">


## 🎯 API Endpoints
| endpoint | HTTP Method | 기능 | 설명 |
|----------|-------------|------|-------------------|
|/app/product | GET | 기프티콘 조회 |  구매/판매 할 수 있는 기프티콘을 조회한다.
|/app/sale | GET | 웨이팅 내역 조회 | 판매 대기중인 기프티콘을 조회한다.
|/app/sale/:user_id | POST | 기프티콘 판매 | 판매 등록 기능.</br> 판매 가능한 상태가 아닌 경우에는 웨이팅 내역으로 등록된다.
|/app/order/:product_id | PATCH | 기프티콘 구매 | 기프티콘 잔여 개수와 웨이팅 번호를 조절한다.


## 📚 ERD
![](https://velog.velcdn.com/images/miracle-21/post/6ed8cd60-9862-4c02-9d15-6a8700bf1c65/image.png)


## 🔖 API 명세서
- [postman API 링크](https://documenter.getpostman.com/view/18832289/2s8YRmKDCu)

![](https://velog.velcdn.com/images/miracle-21/post/9bbd3de8-d002-4517-ae62-9ae79c86839d/image.gif)
