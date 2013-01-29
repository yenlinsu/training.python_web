# 1. Use Facebook Graph API to get name and location of friends
# 2. Parse the data obtained from Facebook Graph API and scrub it to the desired format
# 3. Plug the locations of my friends on Google Map using Google static map API

import json, urllib2, pprint, webbrowser

def get_mapping(url):
    """Get the rank of the name from names.whitepages.com"""
    page = urllib2.urlopen(url)
    html = page.read()
    parsed = BeautifulSoup(html)
    entry = parsed.find('table', class_='rank inline_block')
    rank = entry.attrs['title'].split()[3][:-2]
    return rank

def scrub_data(f_dic_u):
    """Scrub the unicode dictionary passed in and returned a dictionary normalized sorted in different ways"""
    new_dic = dict()
    for element in f_dic_u['data']:
        if 'location' in element:
            loc = element['location']['name'].encode('ascii','ignore')
            name = element['name'].encode('ascii','ignore')

            # Dictionary with name as the key and location as the value
            #new_dic[name] = loc

            # Inverse dictionary with location as the key and a list of names as value
            #if loc not in new_dic:
            #    new_dic[loc] = [name]
            #else:
            #    new_dic[loc].append(name)

            # Inverse dictionary with location as the key and a number of count of names as value
            if loc not in new_dic:
                new_dic[loc] = 1
            else:
                new_dic[loc] += 1

    return new_dic

    # Return only the top 3 locations
    #top3_loc = dict()
    #for key in new_dic:
    #    if new_dic[key] >= 10:
    #        top3_loc[key] = new_dic[key]

    #return top3_loc

def parse_data(file):
    f = open(file, 'r')
    f_dic = json.loads(f.read())
    f.close()
    return f_dic

def print_map(f_dic):
    new = 2
    url_1 = 'http://maps.googleapis.com/maps/api/staticmap?center=honolulu,hawaii,hi&zoom=2&size=640x640&scale=2&markers=color:green'
    for key in f_dic:
        loc, num = key, f_dic[key]
        url_1 += '|%s' % loc

    url_final = url_1 + '&sensor=false'
    print url_final
    webbrowser.open(url_final,new=new)

def main():
    fb_dic_u = parse_data('AllenFBfriendslocation.txt')
    fb_dic = scrub_data(fb_dic_u)
    pprint.pprint(fb_dic)
    print_map(fb_dic)

if __name__ == '__main__':
    main()