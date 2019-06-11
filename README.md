# fx_prediction
Predict fx and earn 5 oku.

## Dataset

### Introduction

<u>**what is the tickdata?**</u>

A tick-by-tick market data which is characterized by each single 'event' (transaction, quote, price movement, etc.) or one logical unit of information.

<u>**why NOT MT5(MetaTrader 5)?**</u>

* Sometimes miss data
  * Due to a trable in server, client and networks.
* Network latency
  * MT5 server returns the system time of when ping receive. (the delay time between JP and NY is about 100-200ms)
  * Provided data has no timestamp.
* History center has only per minute data

<u>**why Dukascopy?**</u>

* A bank and market maker in Switzerland
* Established and trusted as a broker
* No registration required and free
* Latest data of 1 hour ago is available
* Highly reliable data

### How to download

[Here](https://github.com/giuse88/duka) is the all things.

#### References

* [High frequency data](https://en.wikipedia.org/wiki/High_frequency_data)
* [MetaTrader 5](https://www.metatrader5.com/en)
* [Download tickdata from dukascopy](https://www.slideshare.net/mobile/NakataMaho/tickdata)
* [duka](https://github.com/giuse88/duka)
