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

  listitem_video22 = xbmcgui.ListItem(' part 01 أحداث خاصة', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/events//index.1.rss', listitem_video22, True)
  
  listitem_video22 = xbmcgui.ListItem(' part 02 أحداث خاصة', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/events//index.2.rss', listitem_video22, True)
  
  listitem_video22 = xbmcgui.ListItem(' part 03 أحداث خاصة', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/events//index.3.rss', listitem_video22, True)

  listitem_video22 = xbmcgui.ListItem('عظات مُصورة 01', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/video/index.1.rss', listitem_video22, True)

  listitem_video23 = xbmcgui.ListItem('عظات مُصورة 02 ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/video/index.2.rss', listitem_video23, True)
  
  listitem_video23 = xbmcgui.ListItem('عظات مصورة 03 ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/video/index.3.rss', listitem_video23, True)
  
  listitem_video23 = xbmcgui.ListItem('عظات مصورة 04', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/video/index.4.rss', listitem_video23, True)
  
  listitem_video24 = xbmcgui.ListItem('برنامج من حقك تفهم ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/understand/index.1.rss', listitem_video24, True)

  listitem_video25 = xbmcgui.ListItem('حقيقة إيمانى part 1 ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/myfaith/my-faith1/index.1.rss', listitem_video25, True)

  listitem_video25 = xbmcgui.ListItem('حقيقة إيمانى part 2 ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/myfaith/my-faith1/index.2.rss', listitem_video25, True)
  
  listitem_video26 = xbmcgui.ListItem('حقيقة إيمانى part 3 ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/myfaith/my-faith2/index.1.rss', listitem_video26, True)

  listitem_video27 = xbmcgui.ListItem('حقيقة إيمانى part 4', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/myfaith/my-faith2/index.2.rss', listitem_video27, True)

  listitem_video28 = xbmcgui.ListItem('سيمنار تربية الأطفال - د. نورا إدوارد part 1', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/child-nora/index.1.rss', listitem_video28, True)

  listitem_video29 = xbmcgui.ListItem('سيمنار تربية الأطفال - د. نورا إدوارد part 2 ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/audio-video/tvprogram/child-nora/index.2.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('أولادنا وكيف نربيهم - د. أوسم ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/the-family/bringing-up-children/child-awsam/index.1.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('سمينار تربية الأطفال ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/the-family/bringing-up-children/child-seminar/index.1.rss', listitem_video29, True)
  
  listitem_video28 = xbmcgui.ListItem('سمينار الإرتباط - م.هانى أسعد', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/the-family/marriage/marriage-seminar/index.1.rss', listitem_video28, True)

  listitem_video29 = xbmcgui.ListItem('سمينار المشاكل الزوجية ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/the-family/marriage/mashakel-zawgya/index.1.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('سيمنار - زواج على الصخر ', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/the-family/marriage/marriageontherock/index.1.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('Testimonies 01', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/testimonies/index.1.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('Testimonies 02', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/testimonies/index.2.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('إسرائيل بين الماضى و الحاضر', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/spec-studies/israel/index.1.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('الشعور بالذنب - د.أوسم وصفى', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/spec-studies/sico-problems/guilt/index.1.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('العلاقات الإعتمادية', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/spec-studies/sico-problems/dep-relations/index.1.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('الغضب - د.أوسم وصفى', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/spec-studies/sico-problems/anger/index.1.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem(' الخليقة بين العلم و الإيمان', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/spec-studies/scienceandfaith/s_fconfrence/index.1.rss', listitem_video29, True)
  
  listitem_video29 = xbmcgui.ListItem('Drama', thumbnailImage=__icon__)
  xbmcplugin.addDirectoryItem(int(sys.argv[1]), 'http://www.kdec.net/feed/church-services/drama/index.1.rss', listitem_video29, True)
  

  xbmcplugin.setContent(int(sys.argv[1]), 'episodes')

  # End of list...
  xbmcplugin.endOfDirectory(int(sys.argv[1]), True)

Main()
