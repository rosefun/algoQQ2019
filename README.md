### Algorithm competition of Tencent  

**1. Introduce**

[Here](https://algo.qq.com/) is the competition link.

**2. Dataset**

* **totalExposureLog.out**

  This is history exposure log data file. It was selected to be uniformly sampled in one-512th of the user dimension .

  e.g.

  ```
  requestId timestamp adId userId exposureId size bid pctr quality_ecpm totalEcpm
  53991770	1550409746	94	1160618	451525	50	46	47.217	944.34	3122.34
  ```



$bid * pctr + quality\_ecpm = totalEpm$ .

