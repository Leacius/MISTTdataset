# Table Tennis Match Video Dataset

This dataset is an official extension of the **MISTT Dataset** originally introduced in the paper:  
**[Fine-grained Stroke Recognition in Broadcast Table Tennis Videos with ATDT](https://dl.acm.org/doi/10.1145/3769299)** (ACM TOMM 2024).

---

### Dataset Description

This repository provides an extended video database built upon the foundations of the MISTT project. It incorporates a wider variety of world-class table tennis matches (including WTT Smashes, ITTF World Championships, and the Tokyo Olympics).

The structure of each annotation entry contains the following root keys:

* `index`: The sequential identification number of the annotation entry (starting from `0`).
* `eventType`: The category of the annotated event (`發球`, `動作`).
* `startFrame`: The exact starting frame of the event, synchronized according to the specific **Annotation FPS** of the video.
* `duration`: The total number of frames the event lasts.
* `labels`: A list of detailed attribute key-value pairs (`name`, `type`, `value`) describing the event:
    * **For Serves (`發球`):** Includes `正反手` (拍面).
    * **For Strokes/Actions (`動作`):** Includes `擊球拍面` (拍面), `動作` (動作, e.g., 拉(下旋), 撥球(挑球)/擰拉, 反拉).
 
## Data Alignment & Preprocessing (`YT_json`)

To facilitate direct model training and inference on downloaded YouTube videos, we provide both raw and adjusted frame-aligned annotations:

* **Raw Annotations (`labeled_json/`):** Contains the original human-annotated stroke timestamps based on the native broadcast acquisition frame rates.
* **YouTube-Aligned Annotations (`YT_json/`):** To resolve frame rate discrepancies caused by video downloaders, all annotations in this directory have been converted and frame-aligned to match standard YouTube playback frame rates (typically **30 fps** or **50 fps**). 

> **Note:** Due to frame-rate conversion and rounding, there may be a minor boundary offset of a few frames compared to the raw video.

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

| Index | Match | Video ID | YouTube Link | Annotation FPS |
| :---: | :--- | :---: | :--- | :---: |
| 1 | 2022WTT Smash-成年男子組, 馬龍 VS 林昀儒 | CmbwzmO6PX | [YouTube](https://www.youtube.com/watch?v=jj28xXUKajI) | 25 fps |
| 2 | 2022WTT Star Contender Doha-成年男子組, 林昀儒 VS 林鐘勳 | odugj313m2 | [YouTube](https://www.youtube.com/watch?v=utpCnlKdI5E) | 25 fps |
| 3 | 2022WTT Star Contender ESS-成年男子組, 林昀儒 VS 王楚欽 | 65a7fSWxre | [YouTube](https://www.youtube.com/watch?v=NT4Ua7z8Ldo) | 29.97 fps |
| 4 | 2022WTT冠軍賽布達佩斯站-成年男子組, Hugo Calderano VS 林鐘勳 | i6n6xjDxCk | [YouTube](https://www.youtube.com/watch?v=Cj5jsgcunNU) | 25 fps |
| 5 | 2022WTT冠軍賽布達佩斯站-成年男子組, 莊智淵 VS 梁靖崑 | DbIkSN2KxR | [YouTube](https://www.youtube.com/watch?v=_rHqF6_J5rM) | 25 fps |
| 6 | 2022WTT冠軍賽布達佩斯站-成年男子組, 林高遠 VS 林昀儒 | t7tRSTjQ0O | [YouTube](https://www.youtube.com/watch?v=ePmWAAwukn8) | 25 fps |
| 7 | 2022WTT冠軍賽布達佩斯站-成年男子組, 馬龍 VS Patrick Franziska | dhqtw1pGe1 | [YouTube](https://www.youtube.com/watch?v=mos4Y7y7C_U) | 25 fps |
| 8 | 2021世界桌球錦標賽-成年男子組, 梁靖崑 VS Hugo Calderano | Tj7hSZvhqW | [YouTube](https://www.youtube.com/watch?v=DA0XOjF4s_c) | 50 fps |
| 9 | 2022WTT冠軍賽布達佩斯站-成年女子組, 孫穎莎 VS 付玉 | Bddr8bz4eH | [YouTube](https://www.youtube.com/watch?v=Zwhjy6oEfnI) | 25 fps |
| 10 | 2021世界桌球錦標賽-成年男子組, 樊振東 VS Moregardh | 7O6uCFgpq8 | [YouTube](https://www.youtube.com/watch?v=8G3jFJ6AQ4Y) | 25 fps |
| 11 | 2022WTT冠軍賽布達佩斯站-成年女子組, 陳思羽 VS 伊藤美誠 | wMhfRhWN6S | [YouTube](https://www.youtube.com/watch?v=aPzV1UDpQgM) | 25 fps |
| 12 | 2022WTT冠軍賽布達佩斯站-成年男子組, Timo Boll VS 林高遠 | zzuX0uFxIj | [YouTube](https://www.youtube.com/watch?v=IwV4S7NtxvM) | 25 fps |
| 13 | 2022WTT冠軍賽布達佩斯站-成年女子組, 陳夢 VS 王曼昱 | 4yYvMIVQNZ | [YouTube](https://www.youtube.com/watch?v=QqX9PUm4TFs) | 30 fps |
| 14 | 2022WTT冠軍賽布達佩斯站-成年男子組, Patrick Franziska VS 張本智和 | dgVLPQOFbr | [YouTube](https://www.youtube.com/watch?v=UFIrohRDraQ) | 25 fps |
| 15 | 2022WTT冠軍賽布達佩斯站-成年男子組, 莊智淵 VS 林高遠 | AuhW1I2dZQ | [YouTube](https://www.youtube.com/watch?v=HEG61hfnNEc) | 25 fps |
| 16 | 2022世界桌球團體錦標賽-成年女子組, 王曼昱 VS 伊藤美誠 | nYoaxjNLXd | [YouTube](https://www.youtube.com/watch?v=tpNFTqyHZpo) | 30 fps |
| 17 | 2022WTT冠軍賽布達佩斯站-成年男子組, 張本智和 VS 林鐘勳 | uPQ2hRtPim | [YouTube](https://www.youtube.com/watch?v=ttijyWbB7Rw) | 25 fps |
| 18 | 2021WTT Cup Final Singapore-成年男子組, 林昀儒 VS 王楚欽 | cSM5vGjmEm | [YouTube](https://www.youtube.com/watch?v=53eFyvdHhRA) | 25 fps |
| 19 | 2021WTT Cup Final Singapore-成年男子組, 樊振東 VS 王楚欽 | 4tYoJuM6If | [YouTube](https://www.youtube.com/watch?v=FW5zxl5oMzY) | 25 fps |
| 20 | 2021WTT Cup Final Singapore-成年男子組, 樊振東 VS 張本智和 | Dlh9nMDYzm | [YouTube](https://www.youtube.com/watch?v=u9UcfZ6T71c) | 25 fps |
| 21 | 2022世界桌球團體錦標賽-成年男子組, 王楚欽 VS 張本智和 | eXZe1cgNmk | [YouTube](https://www.youtube.com/watch?v=BGBp3eUYdc4) | 30 fps |
| 22 | 2022Singapore Smash-成年男子組, 馬龍 VS 王楚欽 | Lu9I2SrfHe | [YouTube](https://www.youtube.com/watch?v=asj-b47Bc-c) | 25 fps |
| 23 | 2022WTT Cup Finals XinXiang-成年女子組, 王曼昱 VS 陳夢 | aNgTF2Dol5 | [YouTube](https://www.youtube.com/watch?v=6dgbQQMChCg) | 30 fps |
| 24 | 2022WTT冠軍賽布達佩斯站-成年男子組, 張本智和 VS 林高遠 | ijzGS7HBBS | [YouTube](https://www.youtube.com/watch?v=6dgbQQMChCg) | 25 fps |


---

## Citation

If you find this dataset or codebase useful in your research, please consider citing the original paper and this dataset extension:

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
