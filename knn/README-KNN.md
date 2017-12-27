# k-Nearest Neighbors (kNN) Algorithm

kNN 알고리즘은 label 이 있는 data 를 사용하여 classification 을 하는 Supervised Learning 의 한 종류이다.
여기서 k 는 **몇 번째로 가까운 데이터까지 살펴볼 것인가** 를 나타낸다.
kNN 에서 사용하는 거리 측정은 [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) 를 사용한다.

* Euclidean distance
```
\sqrt{\sum_{i=1}^{n}(q_{i}-p_{i})^{2}}
```

## kNN 의 장점
* 알고리즘이 간단 (구현하기 쉬움)
* 수치형, 명목형 값 데이터 분류에 성능이 좋음
* 오류 데이터 (outlier) 에 둔감
* 데이터에 대한 가정이 없음

## kNN 의 단점
* 계산 비용이 높음
* 많은 메모리 요구

## kNN 동작
pre-condition:
* label data set for training

process:
1. label 이 없는 data
2. training set 과 비교
3. 가장 근접한 이웃의 분류 항목을 확인 (상위 k 개)

post-condition:
* k 개의 가장 유사한 데이터들 중 majority vote 를 통해 새로운 데이터 분류를 결정
