# Elasticsearch


### Elasticsearch란?
- 광범위한 개방형 검색 플랫폼
- HTTP의 json 인터페이스 지원
- 다양한 프로그래밍 언어 지원 

### Elasticsearch 용도
- 검색엔진
- 분석 및 인사이트 제공 (어떤 데이터를 적재하는지에 따라 다양한 분석이 가능)
  - 로그 분석
  - 이벤트 분석
  - 성능 분석
- 머신 러닝

**엘라스틱 스택**
- Elasticsearh의 오픈소스 프로젝트
  - 데이터 소스 수집부터 시각화까지의 end to end 스택
  - 로그 수집을 위한 logstash
  - 시각화, 분석을 위한 kibana
  - 네트워크 데이터, 시스템 지표, 성능, 로그를 위한 filebeat

### Elasticsearch 특징
- 기본적인 용도 - 검색 및 집계
- 동적 스키마(자동 생성)
- REST API 인터페이스
- 분산 적재(샤딩)
- 트랜잭션 미지원
- JOIN 미지원

### Elasticsearch 요청과 응답
- 모든 동작을 REST API로 제공
- 입력 -> PUT
- 조회 -> GET
- 삭제 -> DELETE
- 수정 -> POST

### Elasticsearch 기본 요소

**인덱스**는 elasticsearch에서 관련된 문서가 저장되는 데이터베이스의 역할을 한다. 만약 book이라는 인덱스가 있다면 책과 관련된 여러 문서를 포함할 수 있다.

<br>

**문서**는 실제 데이터를 포함하는 JSON 객체로 다음의 예시를 들 수있다.
```json
{
  "title": "엘라스틱 서치 알아보기",
  "author": "ithingv34",
  "year": 2023
}
```
만약 RDB 테이블이라면 다음과 같이 테이블 스키마를 생성할 수 있다

```mysql
CREATE TABLE books (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255),
  author VARCHAR(255),
  year YEAR
)
```

<br>

**매핑**은 문서 내 필드 구조와 데이터 유형을 정의한다. Elasticsearch가 데이터를 효율적으로 인덱싱하고 검색하는 방법을 이해하는 데 도움이 된다. 인덱스를 만들 때 해당 인덱스 내 문서의 필드 속성을 정의하는 매핑을 제공할 수 있다.


- 예를 들어 "book" 인덱스에 대한 매핑은 "title" 필드가 "text" 유형이고 "author" 필드가 "keyword" 유형이며 "year" 필드가 "int" 유형임을 정의할 수 있다. 이 정보는 Elasticsearch가 데이터를 올바르게 처리하고 분석하는 데 도움이 된다.


- 매핑을 사용하면 텍스트 필드에 대한 분석기 또는 날짜 필드에 대한 사용자 정의 형식과 같은 추가 설정을 정의할 수도 있다.

**RDB와 비교**

|Elasticsearch | RDB|
|:---:|:---:|
|인덱스 | 테이블|
|문서 | 행(ROW) |
|필드 | 열(COL) |
|매핑 | 스키마 |

**인덱스**
- 문서를 저장하는 논리적 단위
- 기존 RDB의 테이블과 유사
- 하나의 인덱스에는 많은 문서들이 포함됨 (모든 문서는 인덱스에 포함됨)
- 하나의 인덱스는 동일한 스키마를 가짐
- 스키마에 따라 인덱스가 달라야함

**매핑**
- 관계형 데이터베이스의 스키마와 유사
- 매핑의 종류
  - 동적 매핑 (다이나믹 매핑)
    - ES가 데이터 타입을 보고 자동으로 매핑
    - 인덱스의 규모가 커지면 성능에 영향을 받음
  - 직접 매핑
    - 인덱스 매핑을 직접하는 것
    - 인덱스 생성 시 매핑 설정
    - 매핑 API 이용

### Elasticsearch 데이터 타입

| 분류 | 타입 | 설명 |
|:---:|:----|:--|
|정수형 | integer, short, byte, long | |
|실수형 | float, double | |
|이진값 | binary | Base64 string 같이 인코딩된 바이너리|
|참/거짓 | boolean | true / false |
| 객체 | object | JSON 객체 |
| IP | ip | IP 주소값
| 텍스트 | text | 전문 검색용, 텍스트 분석기가 텍스트를 분리|
| 텍스트 | keyword | 분석용으로 사용 X, 정렬, 집계에 사용|
| 날짜 | date | 날짜나 시간값 |
| 범위 | integer_range, float_range, ong_range, double_range date_range, ip_range | 최소값과 최대값으로 범위를 설정한 데이터|


### Elasticsearch 인덱스 템플릿

- 동일한 다수의 인덱스를 만들 때 사용
- 인덱스 파티셔닝에서 동일한 인덱스를 매번 설정해야 하는 문제
- 템플릿 생성
  - 템플릿 직접 생성
  - 동적 템플릿
- 기본적인 설정
  - 매핑
  - 세팅
- 템플릿은 새 인덱스부터 적용

### 분석기

<img src="./image/1.png">

- 역 인덱싱 - 긴 텍스트를 잘게 나눠서 인덱싱하는 기술
- 분석기 = 토크나이저 + 캐릭터 필터 + 토큰 필터

- 분석기 구성
    | 분석기 구성 요소 | 설명 |
    |:---:|:----:|
    |Char Filter | 입력을 받은 원본 텍스트 문자열을 추가, 변경, 제거 |
    | Tokenizer | 문자열을 받아서 분리 기준에 따라 문자열을 토큰 분리|
    | Token Filter | 토큰을 추가하거나 수정 및 제거|

**분석기 파이프라인**
<img src="./image/2.png">

[**분석기 처리 예시**](https://www.elastic.co/kr/blog/found-text-analysis-part-1)

<img src="./image/3.png">

1. 원본 문자열
2. HTML Strip (Char Filter)
3. standard Tokenizer
4. lowercase Token Filter
5. stop Token Filter
6. snowball Token Filter

[**내장된 분석기 종류**](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-analyzers.html)

- Standard
  - 기본적으로 사용하는 분석기, 영문법 기준
- Simple
  - 문자만 토큰화
- Whitespace
  - 공백을 기준으로 토큰화
- Stop
  - 스톱 필터 포함
- keyword

[### 토크나이저](https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-tokenizers.html)

- 분석기에 반드시 포함되는 문자열 분리 기능
- Word Oriendted Tokenizer
  - 전체 문장에서의 개별적인 단어로 분리
- Partial Word Tokenizers
  - 부분 단어 일치를 위해 텍스트, 단어를 조각냄
- Structured Text Tokenizers
    - 이메일, 주소, 경로와 같은 구조화된 텍스트 분리
   
[### 역인덱스 (Inverted Indexes and Index Terms)](https://www.elastic.co/kr/blog/found-elasticsearch-from-the-bottom-up)

- 책의 **찾아보기** 색인과 유사
- 분리된 단어를 역인덱싱해서 문서를 쉽게 찾을 수 있음
  
<img src="./iamge/4.png">


### Elasticsearch 검색
- 관계형 데이터베이스의 검색 조회(작은 서비스) 그 이상의 검색
- 텍스트 매칭
- 텍스트의 변형 검색
- 스코어링 알고리즘

**쿼리 사용방법**

<img src="./image/5.png">

- 쿼리스트링
  - 한 줄에 들어가는 정도
  - 간단한 쿼리에 사용
  - 길어지면 복잡하고 가독성이 떨어짐
- 쿼리 DSL
  - 한 줄을 넘어가는 복잡한 쿼리
  - 쿼리 전용언어
  - JSON 기반의 언어
  - REST API 요청 본문에 JSON 쿼리 작성

**쿼리 종류**
- 리프 쿼리
  - 특정 필드에서 용어를 검색하는 방식
  - 매치, 용어, 범위
- 복합 쿼리
  - 쿼리를 조합해서 검색하는 방식
  - 논리 쿼리

**쿼리 방식 구분**
- 전문 쿼리(Fulltext query)
  - 텍스트 타입의 필드를 대상(많은 문자열)으로 검색
  - 매치 쿼리, 매치 프레이즈 쿼리, 멀티 매치 쿼리
- 용어 수준 쿼리(Term level query)
  - 키워드, 숫자, 범위 형태의 필드를 대상으로 검색
  - 정확히 그 단어와 순서가 일치해야 검색됨
  - 용어 쿼리, 여러 용어 쿼리
  
### Elasticsearch 집계 기능
- 메트릭 집계
  - 특정한 필드를 기준으로 수치 계산이나 통계값을 구하는 기능
  - avg, min, max, sum, percentiles, stats
- 버킷 집계
  - 특정 기준에 따라 문서를 묶어주는 기능
    - histogram, range, date_range, terms, filters

### Elasticsearch 시스템 용어와 기능
- 클러스터
- 노드
  - Elasticsearch 클라우드를 구성하는 하나의 인스턴스
  - 노드는 여러 역할을 담당할 수 있음
  - 노드 종류
    - 마스터 노드: 클러스터의 모든 정보를 관리하고 담당
    - 데이터 노드: 데이터의 CRUD, 검색, 집계 담당
    - 투표 전용 노드: 마스터 노드 선정에 투표 참여 담당
    - 인제스트 노드: 문서의 가공과 처리를 담당
    - 머신러닝 노드: 머신러닝 기능을 담당
    - 코디네이터 노드: REST API 요청의 처리를 담당
- 샤드
  - 데이터를 나눠 분산 저장, 수평확장, 분산처리
  - 고가용성, 성능향상, 처리량, 처리 속도를 높이는 장점
  - Primary 샤드 - 데이터 원본
  - Replica 샤드 - 데이터의 복제본
  - 샤드 상태
    - **UNASSIGNED**
    - **INITIALIZING**
    - **STARTED**
    - **REPLOCATING**
- 백업
  - 백업은 자주하는 것이 중요
  - Elasticsearch의 백업은 증분 백업이라 자주 백업 가능
  - 저장소
    - 백업을 위한 저장소
      - ex) AWS S3, GCS 등
  - 스냅샷
    - 모든 데이터 저장 또는 특정 인덱스의 데이터만 저장
    - 전체 백업이후에는 증분만 저장 가능
  - 스냅샷 복원
    - 찍어둔 스냅샷을 이용하여 데이터 복원