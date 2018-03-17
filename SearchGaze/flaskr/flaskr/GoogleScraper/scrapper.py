#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Shows how to control GoogleScraper programmatically.
"""

import sys
import json
from GoogleScraper import  GoogleSearchError, scrape_with_config 
from GoogleScraper.database import ScraperSearch, SERP, Link


### EXAMPLES OF HOW TO USE GoogleScraper ###

# very basic usage
def basic_usage():
    # See in the config.cfg file for possible values

    # 'facebook', 'youtube', 'download', 'movies', 'google', 'streaming', 'hotmail', 'facebook login', 'internet', 'yahoo', 'madasfish', 'ebay', 
    # 'antivirus software', 'yahoo mail', 'craigslist', 'aot', 'paid to promote', 'dvd movies online', 'gmail', 'games',
    # 'fb', 'internetreal', 'shopping', 'proxy dozer',
    # 'amazon', 'jobs', 'video', 'promote', 'new', 'twitter', 'paid to', 'minecraft', 'free', 'earn cpcs', 'earn chi', 'netflix', 'videos', 'net', 'pulse', 'posted by',
    #   'date you', 'news', 'this date', 'msn', 'facebook yahoo', 'dating', 'birthday gifts', 'cars', 'best100tattoos', 'walmart', 'lkckclckli1i', 'sports', 'software',
         # 'weather', 'watch online', 'medical insurance', 'dating websites', 'in', 'movies online', 'friv', 'aol', 'search', 'houses for rent by owner', 'of', 'internet marketing',
    # 'blogging make money', 'make money blogging', 'game', 'movie2k', 'walmart stores', 'credit card', 'instagram', 'internet marketing advertising', 'biz', 'travel', 'to',
    #        'dating website', 'windows', 'quick weight loss diet', 'omegle', 'comment', 'tips lose weight', 'account', 'health', 'business', 'free photography stock', 'exercise', 'f',
    #         'computers', 'personal loan', 'hotel', 'stock', 'entertainment', 'pixnet.net', 'thephoenix-forums', 'pandora', 'xanax', 'quick weight loss diets', 'foxloveyo.pixnet.net',
    # 'dailymotion', 'best morning workout', 'a', 'college', 'mapquest', 'clomid', 'undefined', 'diet', 'dating sites', 'tumblr', 'coupons', 'shoes', 'security systems', 'personal loans',
    #           'finance', 'bank', 'search engine', 'maps', 'watch movies online', 'online relationship advice', 'for', 'wells fargo', 'fitness', 'security system', 'payday loans', 'google chrome',
    #            'ultram', 'le bon coin', 'bank of america', 'pinterest', 'electronics', 'register domain name free', 'and', 'car', 'technology', 'how', 'auto', 'robots.txt', 'g', 'full movie',
    # 'real estate', 'galaxyshelp', 'free download', 'project free tv', 'restaurants', 'espn', 'computer', 'business opportunities', 'chase', 'dvd movies', 'loans', 'save your marriage',
    #             'google translate', 'photos', 'art', 'gifts', 'exchange links', 'tv', 'santa barbara community college', 'what', 'society', 'speed test', 'sport', 'bing', 'watch full movies online',
    #              'science', 'target', 'car insurance companies', 'web hosting services', 'medical insurances', 'flowers', 'mobile', 'services', 'football', 'aviator 10 cinema', 'university', 'social',
    # 'webzi', 'school', 'wikipedia', 'watch', 'cosmetics and makeup', 'happy wheels', 'downloading', 'colleges', 'phone', 'watch online full films', 'blog', 'make money online', 'skype',
    #                'money', 'by country', 'exercises', 'account options', 'you', 'paypal', 'social network', 'dvd tv series', 'itunes', 'watch tv shows', 'coach', 'windows xp', 'watch sports tv online',
    #                 'firefox', 'youtube to mp3', 'viagra', 'putlocker', 'free antivirus download', 'letmewatchthis', 'autotrader', 'home depot', 'vacation', 'dvd rental', 'nod322', 'dictionary',
    # 'search youtube', 'translate', 'fa', 'free games', 'pirate bay', 'free virus protection', 'check', 'flights', 'xml win data web', '2013', 'windows media player', 'roblox', 
    #                 'torrent', 'gumtree', 'ebay uk', 'outlook', 'pof', 'payday loan', 'be careful with my heart', 'diet nutrition', 'pictures', 'lowes', 'debt', 'your email address', 'marketing',
    #                  'torrent download', 'movie watch online', 'sale', 'images', 'english', 'linkedin', 'city', 'data recovery', 'free online dating sites', 'credit', 'youtube videos',
    # 'free stock photography', 'ebook library', 'casino', 'food', 'webcam girls', 'hotel in hollywood', 'iphone', 'justin bieber', 'internet service provider', 'for windows',
    #                    'video watch', 'single', 'hotel in singapore', 'hong kong hotel', 'speedtest', 'homes', 'is', 'social networking site', 'download flash macromedia player', 'diet loss quick weight', 
    #                    'sponsors', 's', 'tablet', 'hotels', 'loss weight', 'shows', 'testing iq', 'chatroulette', 'film', 'code', 'va loans', 'cnn', 'cheap college football tickets', 'singapore hotel',
    # 'watch sports tv', 'female formal wear', 'player', 'latest movies on dvd', 'web tool', 'website', 'facebook com', 'register domain names', 'isp', 'the best music download sites',
    #                       'cory monteith', 'dvd', 'sony', 'libero', 'education', 'most popular sites', 'miniportal', 'uni', 'online games for free', 'free antivirus downloads', 'education loans', 'webbacklinks',
    #                        'xbox', 'payday cash advance', 'top', 'map', 'megashare', 'online free', 'pinoy ako', 'share', 'health care plan', 'youtube converter', 'gold investments', 'google site search', 'kijiji',
    #                         'savings account interest rates', 'free online dating site', 'indeed', 'furniture', 'miniclip', 'water', 'laptops', 'domain name', 'tattoo the best', 'personal', 'web hosting', 'selena gomez',
    #                          'best buy', 'comcast', 'tablets', 'hydrocodone', 'big brother 15', 'business opportunity', 'kayak', 'hosting', 'moviestarplanet', 'gold investment', 'related', 'new car loan rates', 'hollywood hotel'
    search_strs = [ 'online college degree', 'online college degrees', 'rosalind franklin', 'restaurant', 'worldstarhiphop', 'test', 'single women', 'health insurance', 'whale watching san francisco', 'y', 'published',
                               'buzzcustomcom', 'on', 'web design', 'personal injury lawyer', 'book', 'cube world', 'classifieds', 'broadband plans', 'wedding', 'show', 'fast pass tv', 'picture', 'payday cash advances', 'cheap flights',
                                'digital cameras', 'live cricket streaming', 'hotel in hong kong', 'orange', 'image', 'email', 'daily mail', 'wtakumi', 'credit cards', 'ryanair', 'address', 'web hosting servers', 'episode', 'utorrent'
                                 'stocks', 'goo', 'friends', 'diet pill', 'informationwebportal24', 'baby', 'diet pills', 'c', 'contact', 'argos', 'traduttore', 'm', 'full movies', 'winrar', 'student', 'addiction treatment', 'kate middleton',
                                  'big brother', 'miley cyrus', 'flash player', 'twitter marketing strategy', 'with', 'android', 'pompey online', 'love', 'wallpaper', 'big brother spoilers', 'photo', 'sears', 'transcendental meditation',
                                   'life insurance leads free', 'diet and nutrition', 'vacations', 'free movies online', 'medical', 'dvd movies download', 'sales', 'lyrics', 'advice relationship', 'mlm companies', 'login', 'b', 
                                   'recent posts', 'addiction treatments', 'alcohol treatment', 'calculator', 'entertainments', 'libero mail', 'page', 'online games', 'aol mail', 'sky tv', 'mozilla firefox', 'windows media players',
                                    'hardware', 'home work', 'window', 'individual health insurance wisconsin', 'health care plans', 'watch tv series online', 'file size', 'file', 'all rights reserved', 'apple', 't', 'hotel singapore', 
                                    'facebook benvenuto', 'live cricket', 'insurance companies', 'animal', 'capital one', 'home shopping network', 'web tv film movies free annex', 'hot', 'fox news', 'hair', 'security', 'free downloads'
                                    'photo galleries', 'ways to make money online', 'qinono', 'server', 'let me watch this', 'homing', 'clothing', 'girls', 'savings account interest rate', 'h', 'poptropica', 'auto insurance', 'house', 'twitter for business', 'mail']

    for search_str in search_strs:
        config = {
            #'SCRAPING': {
                'use_own_ip': 'False',
                'keyword': search_str,
                'search_engines': 'bing',
                'num_pages_for_keyword': 4, 
                #'output-filename':'output.json',
            #},
            #'SELENIUM': {
                'sel_browser': 'chrome',
            #},
            #'GLOBAL': {
                'do_caching': 'False'
            #}
        }

        try:
            sqlalchemy_session = scrape_with_config(config)
        except GoogleSearchError as e:
            print(e)

        # let's inspect what we got

        for search in sqlalchemy_session.query(ScraperSearch).all():
            for serp in search.serps:
                print(serp)
                for link in serp.links:
                    print(link)

        with open("results/" + search_str, mode='w', encoding='utf-8') as f:
            for serp in search.serps:
                for link in serp.links:
                    output = {'link':str(link.link), 'title':str(link.title), 'description':str(link.snippet), 'rank':str(link.rank)} 
                    json.dump(output, f)                


# simulating a image search for all search engines that support image search
# then download all found images :)
def image_search():
    target_directory = 'images/'

    # See in the config.cfg file for possible values
    config = {
        'SCRAPING': {
            'keyword': 'beautiful landscape', # :D hehe have fun my dear friends
            'search_engines': 'yandex,google,bing,baidu,yahoo', # duckduckgo not supported
            'search_type': 'image',
            'scrapemethod': 'selenium'
        }
    }

    try:
        sqlalchemy_session = scrape_with_config(config)
    except GoogleSearchError as e:
        print(e)

    image_urls = []
    search = sqlalchemy_session.query(ScraperSearch).all()[-1]

    for serp in search.serps:
        image_urls.extend(
            [link.link for link in serp.links]
        )

    print('[i] Going to scrape {num} images and saving them in "{dir}"'.format(
        num=len(image_urls),
        dir=target_directory
    ))

    import threading,requests, os, urllib

    class FetchResource(threading.Thread):
        """Grabs a web resource and stores it in the target directory"""
        def __init__(self, target, urls):
            super().__init__()
            self.target = target
            self.urls = urls

        def run(self):
            for url in self.urls:
                url = urllib.parse.unquote(url)
                with open(os.path.join(self.target, url.split('/')[-1]), 'wb') as f:
                    try:
                        content = requests.get(url).content
                        f.write(content)
                    except Exception as e:
                        pass
                    print('[+] Fetched {}'.format(url))

    # make a directory for the results
    try:
        os.mkdir(target_directory)
    except FileExistsError:
        pass

    # fire up 100 threads to get the images
    num_threads = 100

    threads = [FetchResource('images/', []) for i in range(num_threads)]

    while image_urls:
        for t in threads:
            try:
                t.urls.append(image_urls.pop())
            except IndexError as e:
                break

    threads = [t for t in threads if t.urls]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    # that's it :)

### MAIN FUNCTION ###

# if __name__ == '__main__':

#     usage = 'Usage: {} [basic|image]'.format(sys.argv[0])
#     if len(sys.argv) != 2:
#         print(usage)
#     else:
#         arg = sys.argv[1]
#         if arg == 'basic':
#             basic_usage()
#         elif arg == 'image':
#             image_search()
#         else:
#             print(usage)

basic_usage()