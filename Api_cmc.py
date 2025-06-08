from requests import get
from tkinter import *
import webbrowser

window = Tk()
window.title('Crypto Prices - 15s')
window.resizable(False,False)
window.geometry('300x117+1611+892')

btc_icon = PhotoImage(file='btc.png')
cmc_icon = PhotoImage(file='cmc_icon.png')
eth_icon = PhotoImage(file='eth.png')

window.iconphoto(True,cmc_icon)

api = '<-- PUT YOUR API KEY HERE -->'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'limit':'5',
  'convert':'USD'
}

headers = {
  'X-CMC_PRO_API_KEY': '<-- PUT YOUR API KEY HERE -->',
}

cryptos = get(url,params=parameters, headers=headers).json()

def crypto_prices(id):
  price = round(float(cryptos['data'][id]['quote']['USD']['price']),2)
  return price

def a_btc():
    webbrowser.open('https://coinmarketcap.com/currencies/bitcoin/')

def a_eth():
    webbrowser.open('https://coinmarketcap.com/currencies/ethereum/')

btc_img = Label(window, image=btc_icon)
btc_img.place(x=5,y=5)

btc_price = Label(window, text=crypto_prices(0), font=('arial',11,'bold'))
btc_price.place(x=56,y=16)

btc_more = Button(window, text='More...', command=a_btc)
btc_more.place(x=230,y=13)

btc_starting_price = crypto_prices(0)

btc_price_change = Label(window, text='0,00%',foreground='#8f8f8f',font=('arial',11,'bold'))
btc_price_change.place(x=168,y=16)

btc_launch_price = Label(window,text=f'Start price: {btc_starting_price}$',font=('arial',7,'bold'))
btc_launch_price.place(x=55,y=2)


eth_img = Label(window, image=eth_icon)
eth_img.place(x=5,y=68)

eth_price = Label(window, text=f'{crypto_prices(1)} USD', font=('arial',11,'bold'))
eth_price.place(x=56,y=78)  

eth_more = Button(window, text='More...', command=a_btc)
eth_more.place(x=230,y=76)

eth_starting_price = crypto_prices(1)

eth_price_change = Label(window, text='0,00%',foreground='#8f8f8f',font=('arial',11,'bold'))
eth_price_change.place(x=168,y=78)

eth_launch_price = Label(window,text=f'Start price: {crypto_prices(1)}$',font=('arial',7,'bold'))
eth_launch_price.place(x=55,y=64)


def refresh_price():
    
    cryptos = get(url,params=parameters, headers=headers).json()

    bitcoin = round(float(cryptos['data'][0]['quote']['USD']['price']),2)

    btc_price.config(text=f'{bitcoin} USD')

    if bitcoin > btc_starting_price:
      btc_price_change.config(foreground='#00db2c',text=f'+{round(((bitcoin-btc_starting_price)/btc_starting_price)*100,2)}%')

    elif bitcoin < btc_starting_price:
      btc_price_change.config(foreground='#db0000',text=f'-{round(((btc_starting_price-bitcoin)/btc_starting_price)*100,2)}%')

    elif bitcoin == btc_starting_price:
      btc_price_change.config(text='0,00%',foreground='#8f8f8f')


    ether = round(float(cryptos['data'][1]['quote']['USD']['price']),2)

    eth_price.config(text=f'{ether} USD')

    if ether > eth_starting_price:
      eth_price_change.config(foreground='#00db2c',text=f'+{round(((ether-eth_starting_price)/eth_starting_price)*100,2)}%')

    elif ether < eth_starting_price:
      eth_price_change.config(foreground='#db0000',text=f'-{round(((eth_starting_price-ether)/eth_starting_price)*100,2)}%')

    elif ether == eth_starting_price:
      eth_price_change.config(text='0,00%',foreground='#8f8f8f')

    window.after(15000,refresh_price)
refresh_price()

window.mainloop()