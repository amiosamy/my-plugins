# -*- coding: utf-8 -*-

# Imports
import os, sys, time
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

__settings__ = xbmcaddon.Addon(id='plugin.video.democracynow')
__icon__ = __settings__.getAddonInfo('icon')
__fanart__ = __settings__.getAddonInfo('fanart')
__language__ = __settings__.getLocalizedString

# Fanart
xbmcplugin.setPluginFanart(int(sys.argv[1]), __fanart__)

# Main
def Main():

  listitem_video22 = xbmcgui.ListItem('ِِِالتلمذة', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://xbmc-plugins-amio.googlecode.com/svn/trunk/index.1.rss', listitem_video22, True)
  
  listitem_video22 = xbmcgui.ListItem('سلطان الله ومسئولية الإنسان', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://xbmc-plugins-amio.googlecode.com/svn/trunk/jesus%20personality.rss', listitem_video22, True)
  
  listitem_video22 = xbmcgui.ListItem('الإختبار المسيحي للنصرة', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://xbmc-plugins-amio.googlecode.com/svn/trunk/%D8%A7%D9%84%D8%A5%D8%AE%D8%AA%D8%A8%D8%A7%D8%B1%20%D8%A7%D9%84%D9%85%D8%B3%D9%8A%D8%AD%D9%8A%20%D9%84%D9%84%D9%86%D8%B5%D8%B1%D8%A9.rss', listitem_video22, True)

  listitem_video22 = xbmcgui.ListItem('شخصية المسيح', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://xbmc-plugins-amio.googlecode.com/svn/trunk/%D8%B4%D8%AE%D8%B5%D9%8A%D8%A9%20%D8%A7%D9%84%D9%85%D8%B3%D9%8A%D8%AD.rss', listitem_video22, True)

  listitem_video23 = xbmcgui.ListItem('الإنسان', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://xbmc-plugins-amio.googlecode.com/svn/trunk/%D8%B4%D8%AE%D8%B5%D9%8A%D8%A9%20%D8%A7%D9%84%D8%A7%D9%86%D8%B3%D8%A7%D9%86.rss', listitem_video23, True)
  
  listitem_video23 = xbmcgui.ListItem('شخصية الله ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://xbmc-plugins-amio.googlecode.com/svn/trunk/%D8%B4%D8%AE%D8%B5%D9%8A%D8%A9%20%D8%A7%D9%84%D9%84%D9%87.rss', listitem_video23, True)
  
  listitem_video23 = xbmcgui.ListItem('الروح القدس', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://xbmc-plugins-amio.googlecode.com/svn/trunk/%D8%A7%D9%84%D8%B1%D9%88%D8%AD%20%D8%A7%D9%84%D9%82%D8%AF%D8%B3.rss', listitem_video23, True)
  
  listitem_video24 = xbmcgui.ListItem('مباديء العلاقة مع الله', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://xbmc-plugins-amio.googlecode.com/svn/trunk/index.2.rss', listitem_video24, True)

  listitem_video25 = xbmcgui.ListItem('الكنيسة', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://xbmc-plugins-amio.googlecode.com/svn/trunk/%D8%A7%D9%84%D8%B1%D9%88%D8%AD%20%D8%A7%D9%84%D9%82%D8%AF%D8%B3.rss', listitem_video25, True)

  listitem_video25 = xbmcgui.ListItem('الشركة مع الله', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/myfaith/my-faith1/index.2.rss', listitem_video26, True)
  
  listitem_video26 = xbmcgui.ListItem('الصراع الروحي ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/myfaith/my-faith2/index.1.rss', listitem_video27, True)

  listitem_video27 = xbmcgui.ListItem('شفاء النفس', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/myfaith/my-faith2/index.2.rss', listitem_video28, True)

  listitem_video28 = xbmcgui.ListItem('العلاقات الانسانية', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/child-nora/index.1.rss', listitem_video29, True)
  

  xbmcplugin.setContent(int(sys.argv[1]), 'episodes')

  # End of list...
  xbmcplugin.endOfDirectory(int(sys.argv[1]), True)

Main()
