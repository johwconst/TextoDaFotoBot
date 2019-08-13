# [TextoDaFotoBot](https://t.me/TextoDaFotoBot) 

Ajude:
[PicPay](http://bit.ly/2YZnGqN) | 
[Criptomoedas](http://bit.ly/2ZV2ljB)

[![GitHub Follow](https://img.shields.io/github/followers/johwconst?style=social)](https://github.com/johwconst/)

![Rastreiobot](https://github.com/johwconst/TextoDaFotoBot/blob/master/TextoDaFotoBot.png)

* [Sobre](#sobre)
* [Configurando](#configurando)
* [Executando](#executando)
* [Contato](#contato)

## Sobre

TextoDaFotoBot é um bot para o [Telegram](http://telegram.org) que tem como objetivo ajudar você a capturar o texto
das suas imagens !



## Configurando

Após realizar o donwload do repositorio, realize a instalação das aplicações necessarias:

```
pip install -r requirements.txt
```

O bot ultiliza a Vision uma API da Google Cloud, ela será a responsavel por capturar os textos contidos na foto, A API possui cobranças para sua ultilização, voce pode consultar a documentação e tirar duvidas de ultilização em: [Google Cloud Vision](https://cloud.google.com/vision/docs/)

Substitua os campos: 

`TOKEN_HERE` - Preencha com o Token gerado pelo BotFather

`GOOGLE_CREDENTIAL_HERE` - Preencha com o endereço local (./credentials-key.json) da chave de acesso a API ([Google Cloud](https://console.cloud.google.com/))


## Executando

Para executar o bot basta digitar o seguinte comando:

```
python TextoDaFotoBot.py
```


## Contato

[Telegram](https://telegram.me/johwconst)

[Instagram](https://instagram.com/johwconst)
