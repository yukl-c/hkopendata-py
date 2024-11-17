import requests
from datetime import datetime


def validate_eta(eta):
   try:
       res = datetime.strptime(eta, '%Y-%m-%dT%H:%M:%S%z')
   except ValueError:
       return None

   return res


def get_all_routes():
   url = 'https://rt.data.gov.hk/v2/transport/citybus/route/CTB/'
   response = requests.get(url)
   res = response.json()['data']
   route_list = [x['route'] for x in res]

   return route_list


def get_terminus(route, oi):
   oi_str = 'inbound' if oi == 'I' else 'outbound'
   url = 'https://rt.data.gov.hk/v2/transport/citybus/route-stop/CTB/{}/{}'.format(route, oi_str)
   response = requests.get(url)
   res = response.json()['data']
   if len(res) > 0:
       terminus = res[0]['stop']
       return terminus

   return None


def get_bus_departure(route, stop_id, oi):
   url = 'https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/{}/{}'.format(stop_id, route)
   response = requests.get(url)
   res = response.json()['data']
   eta_list = [validate_eta(x['eta']) for x in res if x['dir'] == oi]
   eta_list = [eta for eta in eta_list if eta]

   return eta_list


# all_routes = get_all_routes()
# term = {r: get_terminus(r, 'I') for r in all_routes[:10]}
#
# print(len(all_routes))
# print(all_routes)
# print(term)

# 'https://rt.data.gov.hk/v2/transport/citybus/route-stop/CTB/930X/inbound'
# https://rt.data.gov.hk/v2/transport/citybus/eta/CTB/002536/930x

# route = '930x'
# stop_id = '002536'
#
# res = get_bus_departure(route, stop_id)
#
#
# print('ok')

print(get_all_routes())