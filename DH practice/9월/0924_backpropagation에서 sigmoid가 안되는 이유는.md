backpropagation에서 sigmoid가 안되는 이유는. 영향도가 줄어들어 0과 1사이의 값으로 없데이트가 전체적으로 이루어져야하는데 sigmoid를 쓰면 앞 부분에만 영향이 미친다.

그래서 ReLU를 씀. 렐루는 0이하는 무조건 0, 0 이상은 실수값을 가지는 실수값을 출력하는 function으로 무한대로 증가 가능.

- 과정은 reLu로 계산을 하다가 마지막에는 결국 0과 1사이로 표현해야하기에 마지막 함수는 sigmoid로 평준화해줌.



gradientdescentoptimizer는 설명하기가 편해서사용한것이고 실제로 사용할 때는 adamoptimizer를 사용.



Xavier = accuracy와 수렴하는 속도가 빠름.