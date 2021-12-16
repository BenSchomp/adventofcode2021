
hex = {
 '0': '0000',
 '1': '0001',
 '2': '0010',
 '3': '0011',
 '4': '0100',
 '5': '0101',
 '6': '0110',
 '7': '0111',
 '8': '1000',
 '9': '1001',
 'A': '1010',
 'B': '1011',
 'C': '1100',
 'D': '1101',
 'E': '1110',
 'F': '1111' }

def decode( data ):
  bin = ''
  for d in data:
    bin += hex[d]

  ( x, part_one, part_two ) = parse_packet( bin )
  print( 'part one:', part_one )
  print( 'part two:', part_two )

def operator( op, values ):
  if op == 0:
    return sum(values)
  elif op == 1:
    result = values[0]
    for v in values[1:]:
      result *= v
    return result
  elif op == 2:
    return min(values)
  elif op == 3:
    return max(values)
  elif op == 5:
    return 1 if values[0] > values[1] else 0
  elif op == 6:
    return 1 if values[0] < values[1] else 0
  elif op == 7:
    return 1 if values[0] ==  values[1] else 0
  else:
    print( 'bad operator:', op )
    exit()

def parse_packet( packet ):
  #print( "\nparse_packet:", packet )
  packet_version = int(packet[0:3], 2)
  packet_type_id = int(packet[3:6], 2)
  i = 6

  if packet_type_id == 4:
    # literal value ... parse groups of 5 until a lead bit '0' signals final group
    val_str = ''
    while True:
      group = packet[i:i+5]
      val_str += group[1:]

      i += 5
      if group[0] == '0':
        break

    value = int(val_str, 2)
    #print( ' ** value:', value )
    return ( packet[i:], packet_version, value )

  else:
    # operator
    length_type_id = packet[i]
    i += 1
    total_version = 0
    sub_values = []

    if length_type_id == '0':
      # next is 15 bits
      sub_packet_length = int(packet[i:i+15], 2)
      i += 15

      sub_packet = packet[i:i+sub_packet_length]
      i += sub_packet_length
      while '1' in sub_packet:
        (sub_packet, sub_version, sub_value) = parse_packet( sub_packet )
        total_version += sub_version
        sub_values.append( sub_value )

      total_value = operator( packet_type_id, sub_values )
      #print( ' [operator result:', total_value, ']' )
      return ( packet[i:], total_version+packet_version, total_value )

    elif length_type_id == '1':
      # next is 11 bits
      num_sub_packets = int(packet[i:i+11], 2)
      i += 11

      packet = packet[i:]
      for n in range(num_sub_packets):
        (packet, sub_version, sub_value ) = parse_packet( packet )
        sub_values.append( sub_value )

      total_value = operator( packet_type_id, sub_values )
      #print( ' [operator result:', total_value, ']' )
      return ( packet, total_version+packet_version, total_value )

    else:
      print( 'unknown I:', I )
      exit()


# --- main ---
decode( 'A20D5CECBD6C061006E7801224AF251AEA06D2319904921880113A931A1402A9D83D43C9FFCC1E56FF29890E00C42984337BF22C502008C26982801009426937320124E602BC01192F4A74FD7B70692F4A74FD7B700403170400F7002DC00E7003C400B0023700082C601DF8C00D30038005AA0013F40044E7002D400D10030C008000574000AB958B4B8011074C0249769913893469A72200B42673F26A005567FCC13FE673004F003341006615421830200F4608E7142629294F92861A840118F1184C0129637C007C24B19AA2C96335400013B0C0198F716213180370AE39C7620043E0D4788B440232CB34D80260008645C86D16C401B85D0BA2D18025A00ACE7F275324137FD73428200ECDFBEFF2BDCDA70D5FE5339D95B3B6C98C1DA006772F9DC9025B057331BF7D8B65108018092599C669B4B201356763475D00480010E89709E090002130CA28C62300265C188034BA007CA58EA6FB4CDA12799FD8098021400F94A6F95E3ECC73A77359A4EFCB09CEF799A35280433D1BCCA666D5EFD6A5A389542A7DCCC010958D85EC0119EED04A73F69703669466A048C01E14FFEFD229ADD052466ED37BD8B4E1D10074B3FF8CF2BBE0094D56D7E38CADA0FA80123C8F75F9C764D29DA814E4693C4854C0118AD3C0A60144E364D944D02C99F4F82100607600AC8F6365C91EC6CBB3A072C404011CE8025221D2A0337158200C97001F6978A1CE4FFBE7C4A5050402E9ECEE709D3FE7296A894F4C6A75467EB8959F4C013815C00FACEF38A7297F42AD2600B7006A0200EC538D51500010B88919624CE694C0027B91951125AFF7B9B1682040253D006E8000844138F105C0010D84D1D2304B213007213900D95B73FE914CC9FCBFA9EEA81802FA0094A34CA3649F019800B48890C2382002E727DF7293C1B900A160008642B87312C0010F8DB08610080331720FC580' )
