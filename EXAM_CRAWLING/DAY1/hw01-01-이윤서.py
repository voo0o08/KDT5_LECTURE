html_example = '''
<div id="seven-day-forecast" class="panel panel-default">
    <div class="panel-heading">
    <b>Extended Forecast for</b>
    <h2 class="panel-title">
                San Francisco CA    </h2>
    </div>
    <div class="panel-body" id="seven-day-forecast-body">
            <div id="seven-day-forecast-container"><div id="headline-container" class="current-hazard" style="margin-left: 124px"><div id="headline-separator" style="top: 34px; height: 131px"></div><div id="headline-info" style="margin-top: 5px" onclick="$('#headline-detail').toggle(); $('#headline-detail-now').hide()"><div id="headline-detail"><div>Coastal Flood Advisory until February 10, 10:00am</div></div><span class="fa fa-info-circle"></span>Click here for hazard details and duration</div><div class="headline-bar headline-advisory " style="top: 40px; left: 19px; height: 125px; width: 890px">
<div class="headline-title">Coastal Flood Advisory</div>
</div></div><ul id="seven-day-forecast-list" class="list-unstyled" style="padding-top: 60px"><li class="forecast-tombstone current-hazard current-hazard-advisory" onclick="$('#headline-detail-now').toggle(); $('#headline-detail').hide()">
<div class="top-bar">&nbsp;<div id="headline-detail-now"><div>Coastal Flood Advisory until February 10, 10:00am</div></div><span class="tab"></span><span class="fa fa-info-circle"></span></div><div class="tombstone-container">
<p class="period-name">NOW until<br>10:00am Sat</p>
<p><img src="DualImage.php?i=nskc&j=nra&jp=80" alt="" title="" class="forecast-icon"></p><p class="short-desc">Coastal Flood Advisory</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Tonight<br><br></p>
<p><img src="DualImage.php?i=nskc&j=nra&jp=80" alt="Tonight: Rain after 4am.  Low around 47. West northwest wind around 11 mph.  Chance of precipitation is 80%." title="Tonight: Rain after 4am.  Low around 47. West northwest wind around 11 mph.  Chance of precipitation is 80%." class="forecast-icon"></p><p class="short-desc">Clear then<br>Rain</p><p class="temp temp-low">Low: 47 &deg;F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Wednesday<br><br></p>
<p><img src="newimages/medium/ra80.png" alt="Wednesday: Rain, mainly before 4pm.  High near 54. West wind 9 to 18 mph becoming south southwest in the morning. Winds could gust as high as 22 mph.  Chance of precipitation is 80%. New precipitation amounts between a tenth and quarter of an inch possible. " title="Wednesday: Rain, mainly before 4pm.  High near 54. West wind 9 to 18 mph becoming south southwest in the morning. Winds could gust as high as 22 mph.  Chance of precipitation is 80%. New precipitation amounts between a tenth and quarter of an inch possible. " class="forecast-icon"></p><p class="short-desc">Rain</p><p class="temp temp-high">High: 54 &deg;F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Wednesday<br>Night</p>
<p><img src="DualImage.php?i=nra&j=nbkn&ip=20" alt="Wednesday Night: A 20 percent chance of rain before 10pm.  Mostly cloudy, with a low around 45. North wind 9 to 14 mph, with gusts as high as 18 mph.  New precipitation amounts of less than a tenth of an inch possible. " title="Wednesday Night: A 20 percent chance of rain before 10pm.  Mostly cloudy, with a low around 45. North wind 9 to 14 mph, with gusts as high as 18 mph.  New precipitation amounts of less than a tenth of an inch possible. " class="forecast-icon"></p><p class="short-desc">Slight Chance<br>Rain then<br>Mostly Cloudy</p><p class="temp temp-low">Low: 45 &deg;F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Thursday<br><br></p>
<p><img src="newimages/medium/bkn.png" alt="Thursday: Partly sunny, with a high near 56. North wind 5 to 15 mph becoming west northwest in the afternoon. Winds could gust as high as 20 mph. " title="Thursday: Partly sunny, with a high near 56. North wind 5 to 15 mph becoming west northwest in the afternoon. Winds could gust as high as 20 mph. " class="forecast-icon"></p><p class="short-desc">Partly Sunny</p><p class="temp temp-high">High: 56 &deg;F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Thursday<br>Night</p>
<p><img src="newimages/medium/nsct.png" alt="Thursday Night: Partly cloudy, with a low around 44. North wind 5 to 9 mph. " title="Thursday Night: Partly cloudy, with a low around 44. North wind 5 to 9 mph. " class="forecast-icon"></p><p class="short-desc">Partly Cloudy</p><p class="temp temp-low">Low: 44 &deg;F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Friday<br><br></p>
<p><img src="newimages/medium/sct.png" alt="Friday: Mostly sunny, with a high near 56." title="Friday: Mostly sunny, with a high near 56." class="forecast-icon"></p><p class="short-desc">Mostly Sunny</p><p class="temp temp-high">High: 56 &deg;F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Friday<br>Night</p>
<p><img src="newimages/medium/nsct.png" alt="Friday Night: Partly cloudy, with a low around 44." title="Friday Night: Partly cloudy, with a low around 44." class="forecast-icon"></p><p class="short-desc">Partly Cloudy</p><p class="temp temp-low">Low: 44 &deg;F</p></div></li><li class="forecast-tombstone">
<div class="tombstone-container">
<p class="period-name">Saturday<br><br></p>
<p><img src="newimages/medium/few.png" alt="Saturday: Sunny, with a high near 59." title="Saturday: Sunny, with a high near 59." class="forecast-icon"></p><p class="short-desc">Sunny</p><p class="temp temp-high">High: 59 &deg;F</p></div></li></ul></div>
<script type="text/javascript">
// equalize forecast heights
$(function () {
    var maxh = 0;
    $(".forecast-tombstone .short-desc").each(function () {
        var h = $(this).height();
        if (h > maxh) { maxh = h; }
    });
    $(".forecast-tombstone .short-desc").height(maxh);
});
</script>    </div>
</div>'''
from bs4 import BeautifulSoup

def	scraping_use_find(html):
    print("[find 함수 사용]")

    length = len(soup.find_all("div",{"class":"tombstone-container"}))
    print("총 tomestone-container 검색 개수:", length)

    period_name = soup.find_all("p",{"class":"period-name"})
    shorts = soup.find_all("p",{"class": "short-desc"})
    low_temps = soup.find_all("p",{"class":"temp-low"})
    high_temps = soup.find_all("p",{"class":"temp-high"})
    imgs = soup.find_all("img")
    cnt = 0
    for i in range(length):
        print('-' * 60)
        print("[Period]:", period_name[i].text)
        print("[Short desc]:", shorts[i].text)
        if i != 0:
            print("[Temperature]:", low_temps[cnt].text if i%2 == 0 else high_temps[cnt].text)
            if i%2 == 0:
                cnt += 1
        print("[Image desc]:", imgs[i]["alt"])

def scraping_use_select(html):
    print("[select 함수 사용]")
    length = len(soup.select(".tombstone-container"))
    print("총 tomestone-container 검색 개수:", length)

    period_name = soup.select(".period-name")
    shorts = soup.select(".short-desc")
    low_temps = soup.select(".temp-low")
    high_temps = soup.select(".temp-high")
    imgs = soup.select('img')
    cnt = 0
    for i in range(length):
        print('-' * 60)
        print("[Period]:", period_name[i].text)
        print("[Short desc]:", shorts[i].text)
        if i != 0:
            print("[Temperature]:", low_temps[cnt].text if i % 2 == 0 else high_temps[cnt].text)
            if i % 2 == 0:
                cnt += 1
        print("[Image desc]:", imgs[i]["alt"])

# main 문
soup = BeautifulSoup(html_example, "html.parser")
print("National Weather Service Scraping")
print('-' * 30)
scraping_use_find(html_example)
scraping_use_select(html_example)