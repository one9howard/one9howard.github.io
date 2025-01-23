import xbmcaddon
addon_id = xbmcaddon.Addon().getAddonInfo('id')

'''#####-----Build File-----#####'''
buildfile = 'https://raw.githubusercontent.com/one9howard/one9howard.github.io/master/resources/text/builds.json'

'''#####-----Notifications File-----#####'''
notify_url  = 'https://raw.githubusercontent.com/one9howard/one9howard.github.io/master/resources/text/notify.txt'

'''#####-----Excludes-----#####'''
excludes  = [addon_id, 'plugin.video.whatever']