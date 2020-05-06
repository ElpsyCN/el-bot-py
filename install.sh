echo "Install mamoe/mirai-console & mamoe/mirai-api-http ..."

function get_latest_release_number() {
  curl --silent "https://github.com/$1/releases/latest" | sed 's#.*tag/\(.*\)".*#\1#'
}

console_latest_version=$(get_latest_release_number "mamoe/mirai-console")
api_latest_version=$(get_latest_release_number "mamoe/mirai-api-http")

wget "https://github.com/mamoe/mirai-console/releases/download/$console_latest_version/mirai-console-$console_latest_version.jar"
wget -P ./plugins "https://github.com/mamoe/mirai-api-http/releases/download/$api_latest_version/mirai-api-http-$api_latest_version.jar"
