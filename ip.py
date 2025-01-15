def calcIp(ip_list):
  if 0 <= int(ip_list[0]) <= 127:
    print('Class A')
    subnet = [255, 0, 0, 0]
    print('Subnet is ', '.'.join(map(str, subnet)))
    first_IP = [str(int(ip_list[i]) & subnet[i]) for i in range(4)]
    print('First IP is ', '.'.join(first_IP))
    last_IP = [str(int(ip_list[i]) | subnet[i]) for i in range(4)]
    print('Last IP is ', '.'.join(last_IP))

  elif 128 <= int(ip_list[0]) <= 191:
    print('Class B')
    subnet = [255, 255, 0, 0]
    print('Subnet is ', '.'.join(map(str, subnet)))
    first_IP = [str(int(ip_list[i]) & subnet[i]) for i in range(4)]
    print('First IP is ', '.'.join(first_IP))
    last_IP = [str(int(ip_list[i]) | subnet[i]) for i in range(4)]
    print('Last IP is ', '.'.join(last_IP))

  elif 192 <= int(ip_list[0]) <= 223:
    print('Class C')
    subnet = [255, 255, 255, 0]
    print('Subnet is ', '.'.join(map(str, subnet)))
    first_IP = [str(int(ip_list[i]) & subnet[i]) for i in range(4)]
    print('First IP is ', '.'.join(first_IP))
    last_IP = [str(int(ip_list[i]) | subnet[i]) for i in range(4)]
    print('Last IP is ', '.'.join(last_IP))

  elif 224 <= int(ip_list[0]) <= 239:
    print('Class D')
    print('Reserved IP')

  else:
    print('Class E')
    print('Reserved IP')


while True:
  ip = input('Enter IP address: (Type \'exit\' to exit the program) ')
  ip_list = ip.split('.')

  if ip == 'exit':
    print('Exiting the program.....')
    break

  if len(ip_list) != 4 or any(not i.isdigit() or int(i) < 0 or int(i) > 255
                              for i in ip_list):
    print('Invalid IP address')
    continue
  calcIp(ip_list)
