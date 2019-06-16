# Dataset

**[Download](https://drive.google.com/drive/folders/1Sm59gPGBOM-nzssWRtXPY8qZq3Hz1IDa?usp=sharing)**

/   |JPY     |USD     |EUR     |CFH     |CAD
---|--------|--------|--------|--------|-----------
JPY|-       |&#10004;|&#10004;|        |
USD|-       |-       |&#10004;|        |
EUR|-       |-       |-       |        |
CFH|-       |-       |-       |-       |
CAD|-       |-       |-       |-       |-

## Binary Format

Each tick data consists of 22 bytes.

/    |UNIX(sec)|UNIX(ms)|ASK|BID|ASK vol|BID vol
-----|---------|--------|---|---|-------|-------
bytes|4        |2       |4  |4  |4      |4

* Little endian
* Timezone is UTC
* ASK/BID should be devide by 1,000,000
