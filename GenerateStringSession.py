import asyncio
import os
import sys
import time
import random

from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError, PhoneCodeInvalidError, PasswordHashInvalidError, PhoneNumberInvalidError
from telethon.network import ConnectionTcpAbridged
from telethon.utils import get_display_name
from telethon.sessions import StringSession

try:
   import requests
   import bs4
except:
   print("[!] Permintaan Tidak Ditemukan. Memuat...")
   print("[!] Bs4 Tidak Ditemukan. Memuat...")

   if os.name == 'nt':
      os.system("python3.8 -m pip install requests")
      os.system("python3.8 -m pip install bs4")
   else:
      os.system("pip3 install requests")
      os.system("pip3 install bs4")


# Sumber Asli https://github.com/LonamiWebs/Telethon/master/telethon_examples/interactive_telegram_client.py #
loop = asyncio.get_event_loop()

class InteractiveTelegramClient(TelegramClient):
    def __init__(self, session_user_id, api_id, api_hash,
                 telefon=None, proxy=None):
        super().__init__(
            session_user_id, api_id, api_hash,
            connection=ConnectionTcpAbridged,
            proxy=proxy
        )
        self.found_media = {}
        print('@AlphaUserBot Selamat datang di Penerima String')
        print('[i] Menghubungkan ke Server Telegram...')
        try:
            loop.run_until_complete(self.connect())
        except IOError:
            print('[!] Terjadi kesalahan saat menyambungkan. Mencoba lagi...')
            loop.run_until_complete(self.connect())

        if not loop.run_until_complete(self.is_user_authorized()):
            if telefon == None:
               user_phone = input('[?] Nomor Telepon Anda (Contoh: +90xxxxxxxxxx): ')
            else:
               user_phone = telefon
            try:
                loop.run_until_complete(self.sign_in(user_phone))
                self_user = None
            except PhoneNumberInvalidError:
                print("[!] Anda Telah Memasukkan Nomor yang Tidak Valid. Silakan masukkan seperti pada contoh. Sampel: +90xxxxxxxxxx")
                exit(1)
            except ValueError:
               print("[!] Anda Telah Memasukkan Nomor yang Tidak Valid. Silakan masukkan seperti pada contoh. Sampel: +90xxxxxxxxxx")
               exit(1)

            while self_user is None:
                code = input('[?] Lima dari Telegram (5) Masukkan Kode Angka: ')
                try:
                    self_user =\
                        loop.run_until_complete(self.sign_in(code=code))
                except PhoneCodeInvalidError:
                    print("[!] Anda Salah Menulis Kode. Silakan coba lagi. [Mencoba Terlalu Banyak Menyebabkan Anda Diblokir]")
                except SessionPasswordNeededError:
                    pw = input('[i] Verifikasi dua langkah terdeteksi. '
                                 '[?] Ketik Kata Sandi Anda: ')
                    try:
                        self_user =\
                            loop.run_until_complete(self.sign_in(password=pw))
                    except PasswordHashInvalidError:
                        print("[!] 2 Anda salah mengetik kata sandi progresif. Silakan Coba Lagi. [Mencoba Terlalu Banyak Menyebabkan Anda Diblokir]")


if __name__ == '__main__':
   print("[i] Alpha String V3\n@AlphaUserBot\n\n")
   print("[1] Otomatis API ID/HASH Penerima")
   print("[2] Dapatkan String\n")
   
   try:
      secim = int(input("[?] Seçim Yapın: "))
   except:
      print("[!] Harap Masukkan Nomor Saja!")

   if secim == 2:
      API_ID = input('[?] API ID\'iniz [Siap Kunci\'Biarkan kosong untuk digunakan]: ')
      if API_ID == "":
         print("[i] Kunci Siap Digunakan...")
         API_ID = 4
         API_HASH = "014b35b6184100b085b0d0572f9b5103"
      else:
         API_HASH = input('[?] API HASH\'iniz: ')

      client = InteractiveTelegramClient(StringSession(), API_ID, API_HASH)
      print("[i] Kunci String Anda Ada Di Bawah!\n\n\n" + client.session.save())
   elif secim == 1:
      numara = input("[?] Nomor telepon Anda: ")
      try:
         rastgele = requests.post("https://my.telegram.org/auth/send_password", data={"phone": numara}).json()["random_hash"]
      except:
         print("[!] Gagal Mengirim Kode. Periksa Nomor Telepon Anda.")
         exit(1)
      
      sifre = input("[?] Masukkan Kode Dari Telegram: ")
      try:
         cookie = requests.post("https://my.telegram.org/auth/login", data={"phone": numara, "random_hash": rastgele, "password": sifre}).cookies.get_dict()
      except:
         print("[!] Kemungkinan Anda salah mengetik kode. Silakan Mulai Ulang Script.")
         exit(1)
      app = requests.post("https://my.telegram.org/apps", cookies=cookie).text
      soup = bs4.BeautifulSoup(app, features="html.parser")

      if soup.title.string == "Create new application":
         print("[i] Anda Tidak Memiliki Aplikasi. Membuat...")
         hashh = soup.find("input", {"name": "hash"}).get("value")
         AppInfo = {
            "hash": hashh,
            "app_title":"Alpha UserBot",
            "app_shortname": "alphaus" + str(random.randint(9, 99)) + str(time.time()).replace(".", ""),
            "app_url": "",
            "app_platform": "android",
            "app_desc": ""
         }
         app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text
         print(app)
         print("[i] Aplikasi berhasil dibuat!")
         print("[i] API ID/HASH alınıyor...")
         newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
         newsoup = bs4.BeautifulSoup(newapp, features="html.parser")

         g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
         app_id = g_inputs[0].string
         api_hash = g_inputs[1].string
         print("[i] Informasi yang Dibawa! Harap Perhatikan Ini.\n\n")
         print(f"[i] API ID: {app_id}")
         print(f"[i] API HASH: {api_hash}")
         try:
            stringonay = int(input("[?] Anda ingin membeli Tali?? [1 Tulis untuk Ya]: "))
         except:
            print("[!] Harap Tulis Nomor Saja!")

         if stringonay == 1:
            client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
            print("[i] Kunci String Anda Ada Di Bawah!\n\n\n" + client.session.save())
         else:
            print("[i] Penghentian Script...")
            exit(1)
      elif  soup.title.string == "App configuration":
         print("[i] Anda Sudah Membuat Aplikasi. API ID/HASH Çekiliyor...")
         g_inputs = soup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
         app_id = g_inputs[0].string
         api_hash = g_inputs[1].string
         print("[i] Informasi Diperkenalkan! Harap Perhatikan Ini.\n\n")
         print(f"[i] API ID: {app_id}")
         print(f"[i] API HASH: {api_hash}")
         try:
            stringonay = int(input("[?] String Apakah Anda ingin membeli?? [1 Tulis untuk Ya]: "))
         except:
            print("[!] Harap Tulis Nomor Saja!")

         if stringonay == 1:
            client = InteractiveTelegramClient(StringSession(), app_id, api_hash, numara)
            print("[i] Kunci String Anda Ada Di Bawah!\n\n\n" + client.session.save())
         else:
            print("[i] Penghentian Script...")
            exit(1)
      else:
         print("[!] Ada yang salah.")
         exit(1)
   else:
      print("[!] pilihan yang tidak diketahui.")
