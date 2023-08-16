import os


__TRAVELER = "[Kamu](tg://user?id={user_id})"
__TEYVAT = f"[Channel](t.me/{os.getenv('CHANNEL_USERNAME')})"
__RULES = """- Akun Telegram {_TRV} harus follow {_TVT} dulu ya, ehe~.
- Akun Telegram {_TRV} harus memiliki username dan foto profil.
- Pesan {_TRV} harus berjumlah minimal 20 karakter dan 5 kata.
- Pakai hastag 

#rpconfess  #rpmenfess  #rpmfs
#rpcurhat  #rprandom  #rpnanyea
#rpgalau  #rpgamon  #rpgabut
#rphates  #rpjokes.
""".format(_TRV=__TRAVELER, _TVT=__TEYVAT)


ON_START_MSG = """
Halo {_TRV}!, selamat datang di {bot_name}.
Aku adalah bot untuk membawa pesan kamu ke alam {_TVT},
{_TRV} kalau mau tau cara kirim pesan ke {_TVT} tinggal tekan tombol di bawah ya, ehe!
""".format(_TRV=__TRAVELER, _TVT=__TEYVAT, bot_name="{bot_name}")


ON_HOWTO_CB = """
{_TRV} tinggal ketik apapun yang kamu mau  ya, tetapi
pesan {_TRV} akan terkirim jika pesan {_TRV} memenuhi syarat di bawah ini:

{_RULE}

Udah itu aja {_TRV}! enjoy flexing gacha dan damage karakter {_TRV} ya, ehe!
""".format(_TRV=__TRAVELER, _TVT=__TEYVAT, _RULE=__RULES)


ON_SUCCESS_POST = """
Hore, pesan {_TRV} telah terkirim ke {_TVT}!
{_TRV} bisa melihatnya dengan menekan tombol di bawah ya~.
""".format(_TRV=__TRAVELER, _TVT=__TEYVAT)


ON_FAILED_POST = """
Yah, pesan {_TRV} belum memenuhi kriteria di bawah ini:

{_RULE}

Jadi Kamu gabisa mengirim pesan {_TRV}, hiks.
""".format(_TRV=__TRAVELER, _TVT=__TEYVAT, _RULE=__RULES)
