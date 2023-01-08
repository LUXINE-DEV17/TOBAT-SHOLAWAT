import os
os.system('clear')
print(f'---> [ PILIH SHOLAWATAN ]')
print(f'->.   1.sholawatan jibril')
print(f'->.   2.sholawatan solla alaikallahu')
print(f'->.   3.sholawat syaikona')
print('->.   4.robi qola')
watan = input(f'(?) pilih jenis sholawatan : ')
if watan in ['1','01']:
    print('->   sedang memutar sholawat...')
    os.popen('play-audio data/ok.mp3')
    ra = input('[enter untuk kembali]')
elif watan in ['2','02']:
            print(f'->   sedang memutar sholawat...')
            os.popen('play-audio data/ccc.mp3')
            ra = input(f'[enter untuk kembali]')
elif watan in ['3','03']:
        print(f'->   sedang memutar sholawat...')
        os.popen('play-audio data/syaikona.mp3')
        ina = input(f'[enter untuk kembali]')
elif watan in ['4','04']:
    print(f'->   sedang memutar sholawat...')
    os.popen('play-audio data/robiqola.mp3')
    ras = input('[teken enter untuk kembali]')