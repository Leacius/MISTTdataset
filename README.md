# Table Tennis Match Video Dataset

This dataset is an official extension of the **MISTT Dataset** originally introduced in the paper:  
**[Fine-grained Stroke Recognition in Broadcast Table Tennis Videos with ATDT](https://dl.acm.org/doi/10.1145/3769299)** (ACM TOMM 2024).

---

### Dataset Description

This repository provides an extended video database built upon the foundations of the MISTT project. It incorporates a wider variety of world-class table tennis matches (including WTT Smashes, ITTF World Championships, and the Tokyo Olympics).

### Detailed Stroke Category

Below is the detailed taxonomy of table tennis strokes annotated in this dataset, categorized by **Forehand (正手)** and **Backhand (反手)** actions along with their corresponding English technical terms:

| English Technical Term | Forehand (正手) | Backhand (反手) |
| :--- | :--- | :--- |
| **Drop shot / Long push** | 擺短 / 劈長 | 擺短 / 劈長 |
| **Sidespin counter** | 晃 | 撇 |
| **Flick / Chiquita** | 撥球 (挑球) | 擰拉 |
| **Spin / Counterdrive / Counterloop** | 拉上旋 / 反拉 / 對拉 | 拉上旋 / 反拉 / 對拉 |
| **Loop** | 拉下旋 | 拉下旋 |
| **Lob** | 放高球 | 放高球 |
| **Attack / Block / Fast drive (loop) / Slam** | 攻 / 擋 / 快帶 / 殺球 | 攻 / 擋 / 反撕 / 彈 (殺球) |
| **Serve** | 發球 | 發球 |
| **Other** | 其他 | 其他 |

```python
ACTION_NAMES_28C = {
    # Forehand (正手)
    0: "正-擺短",        # Forehand - Drop shot
    1: "正-劈長",        # Forehand - Long push
    2: "正-晃/撇",       # Forehand - Sidespin counter
    3: "正-撥球/擰拉",   # Forehand - Flick
    4: "正-拉(下)",      # Forehand - Loop
    5: "正-拉(上)",      # Forehand - Spin
    6: "正-攻",          # Forehand - Attack
    7: "正-擋",          # Forehand - Block
    8: "正-快帶/反撕",   # Forehand - Fast drive
    9: "正-反拉",        # Forehand - Counterdrive
    10: "正-對拉",       # Forehand - Counterloop
    11: "正-放高球",     # Forehand - Lob
    12: "正-殺球",       # Forehand - Slam
    13: "正-發球",       # Forehand - Serves
    
    # Backhand (反手)
    14: "反-擺短",       # Backhand - Drop shot
    15: "反-劈長",       # Backhand - Long push
    16: "反-晃/撇",      # Backhand - Sidespin counter
    17: "反-撥球/擰拉",  # Backhand - Chiquita
    18: "反-拉(下)",     # Backhand - Loop
    19: "反-拉(上)",     # Backhand - Spin
    20: "反-攻",         # Backhand - Attack
    21: "反-擋",         # Backhand - Block
    22: "反-快帶/反撕",  # Backhand - Fast loop
    23: "反-反拉",       # Backhand - Counterdrive
    24: "反-對拉",       # Backhand - Counterloop
    25: "反-放高球",     # Backhand - Lob
    26: "反-殺球",       # Backhand - Slam
    27: "反-發球",       # Backhand - Serves
}
```
 
## Data Alignment & Preprocessing (`YT_json`)

To facilitate direct model training and inference on downloaded YouTube videos, we provide both raw and adjusted frame-aligned annotations:

* **Raw Annotations (`labeled_json/`):** Contains the original human-annotated stroke timestamps based on the native broadcast acquisition frame rates.
* **YouTube-Aligned Annotations (`YT_json/`):** To resolve frame rate discrepancies caused by video downloaders, all annotations in this directory have been converted and frame-aligned to match standard YouTube playback frame rates. 

> **Note:** Due to frame-rate conversion and rounding, there may be a minor boundary offset of a few frames compared to the raw video.
> **Note:** We provide scripts to label player positions (left vs. right), which are available for use if required.

## Dataset Examples & Label Format

To help researchers quickly understand our data structure, below is a real snippet from our annotation label files (e.g., `{match}_data.txt`). 

### Label File Preview 

```text
Player   EventType 正/反拍     動作類型        StartFrame   Duration Index   
---------------------------------------------------------------------------
L        發球       正        發球           39           59       0       
R        動作       反        撥球(挑球)/擰拉    88           22       2       
L        動作       正        拉(上旋)        98           22       4       
R        動作       反        反拉           109          20       6       
L        動作       正        拉(上旋)        119          22       8       
R        動作       反        攻             128          24       10      
L        動作       反        反拉           141          23       12      
R        動作       反        反拉           151          22       14      
L        動作       反        反拉           164          19       16      
```

## Table Tennis Match Video

| Index | Match | Video ID | YouTube Link | Annotation FPS | Transfer FPS |
| :---: | :--- | :---: | :--- | :---: | :---: |
| 1 | 2022WTT Smash-成年男子組, 馬龍 VS 林昀儒 | CmbwzmO6PX | [YouTube](https://www.youtube.com/watch?v=jj28xXUKajI) | 25 fps | 50 fps |
| 2 | 2022WTT Star Contender Doha-成年男子組, 林昀儒 VS 林鐘勳 | odugj313m2 | [YouTube](https://www.youtube.com/watch?v=utpCnlKdI5E) | 25 fps | 25 fps |
| 3 | 2022WTT Star Contender ESS-成年男子組, 林昀儒 VS 王楚欽 | 65a7fSWxre | [YouTube](https://www.youtube.com/watch?v=NT4Ua7z8Ldo) | 29.97 fps | 29.97 fps |
| 4 | 2022WTT冠軍賽布達佩斯站-成年男子組, Hugo Calderano VS 林鐘勳 | i6n6xjDxCk | [YouTube](https://www.youtube.com/watch?v=Cj5jsgcunNU) | 25 fps | 50 fps |
| 5 | 2022WTT冠軍賽布達佩斯站-成年男子組, 莊智淵 VS 梁靖崑 | DbIkSN2KxR | [YouTube](https://www.youtube.com/watch?v=_rHqF6_J5rM) | 25 fps | 50 fps |
| 6 | 2021世界桌球錦標賽-成年男子組, 樊振東 VS 林高遠 | Da3eHy0HU2 | [YouTube](https://youtu.be/ktGt8O0L3EU?si=8PJjcNRHE1rCC51x) | 30 fps | 50 fps |
| 7 | 2022WTT冠軍賽布達佩斯站-成年男子組, 馬龍 VS Patrick Franziska | dhqtw1pGe1 | [YouTube](https://www.youtube.com/watch?v=mos4Y7y7C_U) | 25 fps | 50 fps |
| 8 | 2021世界桌球錦標賽-成年男子組, 梁靖崑 VS Hugo Calderano | Tj7hSZvhqW | [YouTube](https://www.youtube.com/watch?v=DA0XOjF4s_c) | 30 fps | 50 fps |
| 9 | 2022WTT冠軍賽布達佩斯站-成年女子組, 孫穎莎 VS 付玉 | Bddr8bz4eH | [YouTube](https://www.youtube.com/watch?v=Zwhjy6oEfnI) | 25 fps | 50 fps |
| 10 | 2021世界桌球錦標賽-成年男子組, 樊振東 VS Moregardh | 7O6uCFgpq8 | [YouTube](https://www.youtube.com/watch?v=8G3jFJ6AQ4Y) | 25 fps | 50 fps |
| 11 | 2022WTT冠軍賽布達佩斯站-成年女子組, 陳思羽 VS 伊藤美誠 | wMhfRhWN6S | [YouTube](https://www.youtube.com/watch?v=aPzV1UDpQgM) | 25 fps | 50 fps |
| 12 | 2022WTT冠軍賽布達佩斯站-成年男子組, Timo Boll VS 林高遠 | zzuX0uFxIj | [YouTube](https://www.youtube.com/watch?v=IwV4S7NtxvM) | 25 fps | 50 fps |
| 13 | 2022WTT冠軍賽布達佩斯站-成年女子組, 陳夢 VS 王曼昱 | 4yYvMIVQNZ | [YouTube](https://www.youtube.com/watch?v=QqX9PUm4TFs) | 30 fps | 30 fps |
| 14 | 2022WTT冠軍賽布達佩斯站-成年男子組, Patrick Franziska VS 張本智和 | dgVLPQOFbr | [YouTube](https://www.youtube.com/watch?v=UFIrohRDraQ) | 25 fps | 50 fps |
| 15 | 2022WTT冠軍賽布達佩斯站-成年男子組, 莊智淵 VS 林高遠 | AuhW1I2dZQ | [YouTube](https://www.youtube.com/watch?v=HEG61hfnNEc) | 25 fps | 50 fps |
| 16 | 2022世界桌球團體錦標賽-成年女子組, 王曼昱 VS 伊藤美誠 | nYoaxjNLXd | [YouTube](https://www.youtube.com/watch?v=tpNFTqyHZpo) | 30 fps | 30 fps |
| 17 | 2022WTT冠軍賽布達佩斯站-成年男子組, 張本智和 VS 林鐘勳 | uPQ2hRtPim | [YouTube](https://www.youtube.com/watch?v=ttijyWbB7Rw) | 25 fps | 50 fps |
| 18 | 2021WTT Cup Final Singapore-成年男子組, 林昀儒 VS 王楚欽 | cSM5vGjmEm | [YouTube](https://www.youtube.com/watch?v=53eFyvdHhRA) | 25 fps | 50 fps |
| 19 | 2021WTT Cup Final Singapore-成年男子組, 樊振東 VS 王楚欽 | 4tYoJuM6If | [YouTube](https://www.youtube.com/watch?v=FW5zxl5oMzY) | 25 fps | 50 fps |
| 20 | 2021WTT Cup Final Singapore-成年男子組, 樊振東 VS 張本智和 | Dlh9nMDYzm | [YouTube](https://www.youtube.com/watch?v=u9UcfZ6T71c) | 25 fps | 50 fps |
| 21 | 2022世界桌球團體錦標賽-成年男子組, 王楚欽 VS 張本智和 | eXZe1cgNmk | [YouTube](https://www.youtube.com/watch?v=BGBp3eUYdc4) | 30 fps | 30 fps |
| 22 | 2022Singapore Smash-成年男子組, 馬龍 VS 王楚欽 | Lu9I2SrfHe | [YouTube](https://www.youtube.com/watch?v=asj-b47Bc-c) | 25 fps | 50 fps |
| 23 | 2022WTT Cup Finals XinXiang-成年女子組, 王曼昱 VS 陳夢 | aNgTF2Dol5 | [YouTube](https://www.youtube.com/watch?v=6dgbQQMChCg) | 30 fps | 30 fps |
| 24 | 2022WTT冠軍賽布達佩斯站-成年男子組, 張本智和 VS 林高遠 | ijzGS7HBBS | [YouTube](https://www.youtube.com/watch?v=6dgbQQMChCg) | 25 fps | 50 fps |


---

## Citation

If you find this dataset useful in your research, please consider citing the original paper and this dataset extension 😎:

```bibtex
@article{chang2025fine,
  title={Fine-grained Stroke Recognition in Broadcast Table Tennis Videos with ATDT},
  author={Chang, Tang-Chen and Jheng, Duen-Chian and Liang, Hsuan-Ya and Harchan, Bill Louis and Ching, Pu and Tsai, Tsung-Hsun and Chang, Chih-Yi and Wu, Te-Cheng and Li, Yung-Hui and Pan, Tse-Yu and others},
  journal={ACM Transactions on Multimedia Computing, Communications and Applications},
  volume={21},
  number={12},
  pages={1--24},
  year={2025},
  publisher={ACM New York, NY}
}
