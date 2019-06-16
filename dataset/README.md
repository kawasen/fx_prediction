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

Each tick data consists of 24 bytes.

/    |UNIX|ASK|BID|ASK-vol|BID-vol
-----|----|---|---|-------|-------
bytes|6   |4  |4  |5      |5

* Little endian
* Timezone is UTC
* UNIX timestamp needs to be divided by 1,000
* ASK/BID needs to be divided by 1,000,000
