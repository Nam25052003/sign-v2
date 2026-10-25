from urllib.parse import urlencode
import xdynosaur

qs ="WebIdLastTime=1792938240&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20x86_64&browser_version=5.0%20%28X11%3B%20Ubuntu%29&channel=tiktok_web&clientABVersions=70508271%2C73720541%2C77005875%2C77014443%2C77120364%2C77139461%2C77170269%2C77180103%2C77185848%2C77186132%2C77197070%2C77211090%2C77212295%2C77224699%2C77264360%2C77272165%2C77298109%2C77311579%2C77317016%2C77328047%2C77375400%2C77381207%2C77395982%2C77412892%2C77413130%2C70405643%2C71057832%2C71200802%2C73171280%2C73208420%2C74276218%2C74844724%2C75330961&cookie_enabled=true&count=30&data_collection_enabled=false&device_id=7700611085578389000&device_platform=web_pc&focus_state=true&from_page=user&history_len=13&isNonPersonalized=false&is_fullscreen=false&is_page_visible=true&maxCursor=0&minCursor=0&odinId=7700611028778107925&os=linux&priority_region=&referer=&region=VN&root_referer=&scene=151&screen_height=1200&screen_width=1920&targetUserId=7064533262588544001&tz_name=Asia%2FHo_Chi_Minh&user_is_login=false&webcast_language=en"
body_data = {}
body = urlencode(body_data)
user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:157.0) Gecko/20100101 Firefox/157.0"

sign_opts = dict(
    envcode=65,
    canvas=1938040196,
    ubcode=0,
    version="5.3.2",
    scm_version="1.0.0.417",
    total_reqs=46,
    enc_reqs=10,
)

dyno = xdynosaur.encrypt(qs=qs, body="", ua=user_agent)

print(dyno)
print()

decrypted_dyno = xdynosaur.x_dynosaur_decrypt(dyno)
