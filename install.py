from utils.get_release import LatestRelease

mirai_console = LatestRelease('github', 'mamoe', 'mirai-console')
mirai_api_http = LatestRelease(
    'github', 'mamoe', 'mirai-api-http', './plugins')

mirai_console.display_status()
if not mirai_console.is_latest_version_exist():
    mirai_console.download()

mirai_api_http.display_status()
if not mirai_api_http.is_latest_version_exist():
    mirai_api_http.download()
