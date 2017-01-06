#nice trick with counting letter
import pprint

message = '''sjfaghuklfsdhg klhfsghdfslkjghdfsulh glkfsdhg shg;adiofasd;vn cnvalhgughadsjg hfashklghae rlghaf lkghafsljkgh alfkhg'''
count = {}

for character in message.lower():
    count.setdefault(character, 0)
    #defaultne setne, ze pro kazdy charakter, pokud nema
    #jinou hodnotu, nastavi 0
    count[character] += 1

pprint.pprint(count)
