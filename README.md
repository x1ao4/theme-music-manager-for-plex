# plex-themer
使用 plex-themer 可以轻松为 Plex 媒体库内的电影、电视节目、歌手和合集管理主题音乐，它由两个脚本组成：`plex-theme-uploader.py` 用于上传主题音乐，`plex-theme-deleter.py` 用于删除主题音乐。通过 plex-themer 可以为媒体库内的任何电影、电视节目、歌手或合集上传本地音频文件作为主题音乐，也可以用于删除已存在的主题音乐。

使用 Plex Series 代理刮削电视节目时，Plex 会为你的电视节目搜索主题音乐，如果在数据库中找到了，就会自动将其下载至本地，并在你浏览这些电视节目的页面时播放主题音乐（如果你启用了播放主题音乐），这是一个很有意思的功能。但是 Plex 使用的数据库覆盖范围有限，还是有很多电视节目无法匹配到主题音乐，虽然 Plex 提供了[使用本地主题音乐](https://support.plex.tv/articles/200220717-local-media-assets-tv-shows/)的方法，也支持用户[提交主题音乐文件进行投稿](https://support.plex.tv/articles/201572843-tv-theme-music-submissions/)，但操作起来还是有些麻烦。

好在 Plex 有一个很棒的第三方插件：[Themerr-plex](https://github.com/LizardByte/Themerr-plex)。Themerr-plex 会通过 [ThemerrDB](https://github.com/LizardByte/ThemerrDB) 获取电影、电视节目和合集的主题音乐，并将其添加到 Plex 媒体库对应项目的元数据中，而且还提供了一个 WebUI 用来管理主题音乐，如果有项目缺少主题音乐，你可以直接通过 WebUI 的添加按钮向 ThemerrDB 提交主题音乐进行投稿，不过 ThemerrDB 目前仅支持提交 YouTube 的主题音乐视频链接进行投稿，并且需要人工审核，待审核通过后 Themerr-plex 才会在之后的任务中将你投稿的主题音乐下载到本地，由于 Themerr-plex 是直接从 YouTube 下载主题音乐的，对部分地区的用户来说还是有些不便。

无论是 Plex Series 还是 Themerr-plex，都仅支持为存在于 TMDB（部分支持 IMDb）上的项目添加主题音乐，并且都需要使用指定的代理进行刮削。而通过 plex-themer，你可以为任何电影、电视节目、歌手或合集添加主题音乐，包括无法匹配的项目（比如自定义合集），并且无需任何审核，运行脚本后立刻就可以在 Plex 内播放主题音乐，它对资料库所使用的代理也没有任何限制，这样，你就可以无拘无束地为任意项目添加主题音乐啦。

## 示例
将音频文件按照要求命名，并放入指定的文件夹，然后运行 `plex-theme-uploader.py` 即可自动上传对应项目的主题音乐，例如：
```
已成功连接到服务器：x1ao4

已成功为 "云电影" 中的电影 "花木兰 (2020)" 上传主题音乐
已成功为 "电影" 中的电影 "花木兰 (2020)" 上传主题音乐
已成功为 "电影" 中的合集 "漫威（系列）" 上传主题音乐
已成功为 "电视剧" 中的合集 "漫威（系列）" 上传主题音乐
已成功为 "电视剧" 中的合集 "爱奇艺" 上传主题音乐
已成功为 "综艺" 中的合集 "爱奇艺" 上传主题音乐

1. "电影" 中的电影：霹雳娇娃 (2000)
2. "电影" 中的电影：霹雳娇娃 (2019)

请选择要添加主题音乐的项目（多个项目用分号隔开）：2

已成功为 "电影" 中的电影 "霹雳娇娃 (2019)" 上传主题音乐
已成功为 "电影" 中的电影 "功夫熊猫 (2008)" 上传主题音乐
```
运行 `plex-theme-deleter.py` 脚本，输入要删除主题音乐的项目名称，即可删除对应项目的主题音乐，例如：
```
已成功连接到服务器：x1ao4

请输入要删除主题音乐的项目名称（多个名称用分号隔开）：花木兰 (2020)；漫威（系列）；爱奇艺；霹雳娇娃；功夫熊猫

已成功删除 "云电影" 中的电影 "花木兰 (2020)" 的主题音乐
已成功删除 "电影" 中的电影 "花木兰 (2020)" 的主题音乐
已成功删除 "电影" 中的合集 "漫威（系列）" 的主题音乐
已成功删除 "电视剧" 中的合集 "漫威（系列）" 的主题音乐
已成功删除 "电视剧" 中的合集 "爱奇艺" 的主题音乐
已成功删除 "综艺" 中的合集 "爱奇艺" 的主题音乐

1. "电影" 中的电影：霹雳娇娃 (2000)
2. "电影" 中的电影：霹雳娇娃 (2019)

请选择要删除主题音乐的项目（多个项目用分号隔开）：2

已成功删除 "电影" 中的电影 "霹雳娇娃 (2019)" 的主题音乐
已成功删除 "电影" 中的电影 "功夫熊猫 (2008)" 的主题音乐
```

## 运行条件
- 安装了 Python 3.0 或更高版本。
- 安装了必要的第三方库：plexapi。（可以通过 `pip3 install plexapi` 安装）

## 配置文件
在运行脚本前，请先打开配置文件 `config.ini`，参照以下提示（示例）进行配置。
```
[server]
# Plex 服务器的地址，格式为 http://服务器 IP 地址:32400 或 http(s)://域名:端口号
address = http://127.0.0.1:32400
# Plex 服务器的 token，用于身份验证
token = xxxxxxxxxxxxxxxxxxxx
# Plex 元数据的基础目录，用于定位主题音乐的元数据文件
metadata_base_directory = /path/to/Plex Media Server/Metadata/
# 语言设置，'zh' 代表中文，'en' 代表英文
language = zh

[search]
# 是否搜索电影，true 代表搜索，false 代表不搜索
movie = true
# 是否搜索电视节目，true 代表搜索，false 代表不搜索
show = true
# 是否搜索歌手，true 代表搜索，false 代表不搜索
artist = true
# 是否搜索合集，true 代表搜索，false 代表不搜索
collection = true

[mode]
# 上传主题音乐后是否删除原文件，true 代表删除，false 代表上传后将文件移动至 themes 文件夹
delete_after_upload = false
# 连续删除模式的开关，如果设置为 true，可以连续多次请求删除；如果设置为 false，则会在处理请求后结束运行
continuous_mode = true
# 是否在删除主题音乐时删除用户上传的主题音乐（包括所有非 Plex 提供的主题音乐），true 代表删除，false 代表不删除
user_theme = true
# 是否在删除主题音乐时删除 Plex 提供的主题音乐，true 代表删除，false 代表不删除
plex_theme = false
```

## 使用方法
### plex-theme-uploader
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 修改 `uploader.command (Mac)` 或 `uploader.bat (Win)` 中的路径，以指向你保存的 `plex-theme-uploader.py` 脚本。
3. 打开 `config.ini`，填写你的 Plex 服务器地址（`address`）和 [X-Plex-Token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)（`token`），按照需要设置其他配置选项。
4. 将主题音乐的音频文件按照其对应项目在 Plex 媒体库中的名称命名，并移动至 `uploads` 文件夹内。
5. 双击运行 `uploader.command` 或 `uploader.bat` 脚本以执行 `plex-theme-uploader.py` 脚本。
6. 脚本将自动读取 `uploads` 文件夹内的所有文件，并尝试将这些文件作为主题音乐上传到 Plex 服务器上对应的项目中。你可以在控制台查看处理进度，若同一个文件在媒体库内匹配到了多个不同年份的项目（你可以通过在文件名称中包含年份信息来避免这个情况），将会需要你在控制台手动选择需要添加主题音乐的项目，脚本会根据选择上传主题音乐，并继续处理其余文件，待所有文件都处理完毕后，脚本会自动结束运行。

### plex-theme-deleter
1. 将仓库克隆或下载到计算机上的一个目录中。
2. 修改 `deleter.command (Mac)` 或 `deleter.bat (Win)` 中的路径，以指向你保存的 `plex-theme-deleter.py` 脚本。
3. 打开 `config.ini`，填写你的 Plex 服务器地址（`address`）、[X-Plex-Token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/)（`token`）和 Plex 服务器的元数据文件夹目录（`metadata_base_directory`），按照需要设置其他配置选项。
4. 双击运行 `deleter.command` 或 `deleter.bat` 脚本以执行 `plex-theme-deleter.py` 脚本。
5. 输入要删除主题音乐的项目名称（若有多个项目的主题音乐需要删除，请用分号隔开多个名称），按回车。
6. 脚本将尝试定位 Plex 服务器上对应项目的主题音乐元数据文件的存储位置，并删除该文件所在的文件夹。你可以在控制台查看处理进度，若同一个项目名称在媒体库内匹配到了多个不同年份的项目（你可以通过在项目名称中包含年份信息来避免这个情况），将会需要你在控制台手动选择需要删除主题音乐的项目，脚本会根据选择删除主题音乐，并继续处理其余项目名称，待所有项目名称都处理完毕后，脚本会自动结束运行（若 `continuous_mode = false`）。

## 注意事项
- 请确保你提供了正确的 Plex 服务器地址和 X-Plex-Token。
- 请确保你提供了正确的 Plex 元数据目录，你可以参考[这里](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/)找到你的 `Plex Media Server` 文件夹，`Metadata` 文件夹就在该目录下。
- 脚本仅支持中文和英文，请确保你设置了正确的语言。
- 请勿删除 `uploads` 和 `themes` 文件夹，可以删除文件夹内的 `.gitkeep` 文件。
- 若你在删除了 Plex 提供的主题音乐后，想恢复该主题音乐，可以先对项目执行 `取消匹配`，再 `重新匹配` 即可恢复主题音乐。
- 由于 `plex-theme-deleter.py` 是通过文件系统删除主题音乐文件的，请在存储 Plex 元数据的设备上运行该脚本，并确保脚本有足够的权限删除文件。（`plex-theme-uploader.py` 无此限制）
- 在输入项目名称或输入选项时，若需要输入多个值，请使用分号作为分隔符，支持 `；` 或 `;`。
- 在为主题音乐的音频文件命名或输入项目名称时，可以只输入项目名称，也可以包含年份信息，若库中存在多个同名但不同年份的项目，年份信息有助于脚本自动匹配到正确年份的项目，否则将会需要你手动进行选择，添加年份的格式为 `项目名称（年份）` 或 `项目名称 (年份)`。
- 在输入项目名称时，请确保你输入的项目名称与媒体库内的名称一致，否则将导致匹配失败，输入过程中请勿使用删除键删除字符，否则可能会导致识别错误。
- 请确保运行脚本的设备可以连接到你的服务器。
- 请使用服务器管理员账号的 X-Plex-Token 运行脚本，以确保你拥有足够的权限。
<br>

# plex-themer
With plex-themer, you can easily manage theme music for movies, TV shows, artists, and collections in your Plex media library. It consists of two scripts: `plex-theme-uploader.py` for uploading theme music and `plex-theme-deleter.py` for deleting theme music. Through plex-themer, you can upload local audio files as theme music for any movie, TV show, artist, or collection in your media library. It can also be used to remove existing theme music.

When using the Plex Series agent to scrape TV shows, Plex will search for theme music for your TV shows. If found in the database, it will automatically download it locally and play it when you browse these TV shows' pages (if you have Play Theme Music enabled), which is an interesting feature. However, Plex's database coverage is limited, and there are still many TV shows that cannot match theme music. Although Plex provides methods for [using local theme music](https://support.plex.tv/articles/200220717-local-media-assets-tv-shows/) and supports users to [submit theme music files for submission](https://support.plex.tv/articles/201572843-tv-theme-music-submissions/), the operation is still somewhat cumbersome.

Fortunately, Plex has a great third-party plugin: [Themerr-plex](https://github.com/LizardByte/Themerr-plex). Themerr-plex fetches theme music for movies, TV shows, and collections through [ThemerrDB](https://github.com/LizardByte/ThemerrDB) and adds them to the metadata of corresponding items in the Plex media library. It also provides a WebUI to manage theme music. If a item lacks theme music, you can directly submit theme music to ThemerrDB through the WebUI's add button for submission. However, ThemerrDB currently only supports submitting YouTube theme music video links for submission, and manual review is required. After the review is approved, Themerr-plex will download the theme music you submitted to the local system in subsequent tasks.

Both Plex Series and Themerr-plex only support adding theme music to items existing on TMDB (partially supporting IMDb), and both require the use of specified agents for scraping. Through plex-themer, you can add theme music to any movie, TV show, artist, or collection, including items that cannot be matched (such as custom collections), and there is no need for any review. After running the script, you can immediately play theme music in Plex without any restrictions on the agents used by the library, allowing you to add theme music to any item freely.

## Example
Rename the audio files as required and place them in the specified folder. Then, run `plex-theme-uploader.py` to automatically upload the theme music corresponding to the items. For example:
```
Successfully connected to server: x1ao4

Successfully uploaded theme music for Movie "Mulan (2020)" in "Cloud Movies"
Successfully uploaded theme music for Movie "Mulan (2020)" in "Movies"
Successfully uploaded theme music for Collection "Marvel Collection" in "Movies"
Successfully uploaded theme music for Collection "Marvel Collection" in "TV Shows"
Successfully uploaded theme music for Collection "Netflix" in "Variety Shows"

1. Movie "Charlie's Angels (2000)" in "Movies"
2. Movie "Charlie's Angels (2019)" in "Movies"

Please select the item(s) to which you want to add theme music (multiple items separated by semicolons): 2

Successfully uploaded theme music for Movie "Charlie's Angels (2019)" in "Movies"
Successfully uploaded theme music for Movie "Kung Fu Panda (2008)" in "Movies"
```
Run the `plex-theme-deleter.py` script and input the item titles from which you want to delete the theme music. For example:
```
Successfully connected to server: x1ao4

Please enter the title(s) of the item(s) from which you want to delete theme music (multiple titles separated by semicolons): Mulan (2020); Marvel Collection; Netflix; Charlie's Angels; Kung Fu Panda

Successfully deleted theme music for Movie "Mulan (2020)" in "Cloud Movies"
Successfully deleted theme music for Movie "Mulan (2020)" in "Movies"
Successfully deleted theme music for Collection "Marvel Collection" in "Movies"
Successfully deleted theme music for Collection "Marvel Collection" in "TV Shows"
Successfully deleted theme music for Collection "Netflix" in "Variety Shows"

1. Movie "Charlie's Angels (2000)" in "Movies"
2. Movie "Charlie's Angels (2019)" in "Movies"

Please select the item(s) from which you want to delete theme music (multiple items separated by semicolons): 2

Successfully deleted theme music for Movie "Charlie's Angels (2019)" in "Movies"
Successfully deleted theme music for Movie "Kung Fu Panda (2008)" in "Movies"
```

## Requirements
- Installed Python 3.0 or higher.
- Installed required third-party library: plexapi. (Install with `pip3 install plexapi`)

## Config
Before running the script, please open the `config.ini` file and configure it according to the following prompts (examples).
```
[server]
# Address of the Plex server, formatted as http://server IP address:32400 or http(s)://domain:port
address = http://127.0.0.1:32400
# Token of the Plex server for authentication
token = xxxxxxxxxxxxxxxxxxxx
# Base directory of Plex metadata, used to locate metadata files of theme music
metadata_base_directory = /path/to/Plex Media Server/Metadata/
# Language setting, 'zh' for Chinese, 'en' for English
language = en

[search]
# Whether to search for movies, true for search, false for no search
movie = true
# Whether to search for TV shows, true for search, false for no search
show = true
# Whether to search for artists, true for search, false for no search
artist = true
# Whether to search for collections, true for search, false for no search
collection = true

[mode]
# Whether to delete the original file after uploading theme music, true for delete, false for move the file to the themes folder after uploading
delete_after_upload = false
# Switch for continuous deletion mode, if set to true, multiple deletion requests can be made continuously; if set to false, the script will end after processing the request
continuous_mode = true
# Whether to delete user-uploaded theme music when deleting theme music (including all non-Plex provided theme music), true for delete, false for do not delete
user_theme = true
# Whether to delete theme music provided by Plex when deleting theme music, true for delete, false for do not delete
plex_theme = false
```

## Usage
### plex-theme-uploader
1. Clone or download the repository to a directory on your computer.
2. Modify the paths in `uploader.command (Mac)` or `uploader.bat (Win)` to point to the `plex-theme-uploader.py` script you saved.
3. Open `config.ini`, fill in your Plex server address (`address`) and [X-Plex-Token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/) (`token`), and set other configuration options as needed.
4. Rename the theme music audio files according to the titles of the corresponding items in your Plex media library and move them to the `uploads` folder.
5. Double-click `uploader.command` or `uploader.bat` to execute the `plex-theme-uploader.py` script.
6. The script will automatically read all files in the `uploads` folder and attempt to upload these files as theme music to the corresponding items on the Plex server. You can view the processing progress in the console. If the same file matches multiple items with different years in the media library (you can avoid this situation by including year information in the file name), you will need to manually select the items to which you want to add theme music in the console. The script will upload theme music according to your selection and continue processing other files. After all files have been processed, the script will end automatically.

### plex-theme-deleter
1. Clone or download the repository to a directory on your computer.
2. Modify the paths in `deleter.command (Mac)` or `deleter.bat (Win)` to point to the `plex-theme-deleter.py` script you saved.
3. Open `config.ini`, fill in your Plex server address (`address`), [X-Plex-Token](https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/) (`token`), and the directory of the Plex server's metadata folder (`metadata_base_directory`), and set other configuration options as needed.
4. Double-click `deleter.command` or `deleter.bat` to execute the `plex-theme-deleter.py` script.
5. Enter the item titles from which you want to delete theme music (if there are multiple items with theme music to delete, separate the titles with semicolons) and press Enter.
6. The script will attempt to locate the storage location of the theme music metadata files for the corresponding items on the Plex server and delete the folder containing the files. You can view the processing progress in the console. If the same title matches multiple items in the media library (you can avoid this situation by including year information in the title), you will need to manually select the items from which you want to delete theme music in the console. The script will delete the theme music according to your selection and continue processing other titles. After all titles have been processed, the script will end automatically (if `continuous_mode = false`).

## Notes
- Make sure you've provided the correct Plex server address and X-Plex-Token.
- Make sure you've provided the correct Plex metadata directory. You can refer to [here](https://support.plex.tv/articles/202915258-where-is-the-plex-media-server-data-directory-located/) to find your `Plex Media Server` folder, the `Metadata` folder is under this directory.
- The script only supports Chinese and English. Make sure you have set the correct language.
- Do not delete the `uploads` and `themes` folders, but you may delete the `.gitkeep` files inside them.
- If you want to restore Plex-provided theme music after deleting it, you can first `Unmatch` the item and then `Match` it again to restore the theme music.
- Since `plex-theme-deleter.py` deletes theme music files through the file system, please run this script on the device where Plex metadata is stored and ensure that the script has sufficient permissions to delete files. (`plex-theme-uploader.py` does not have this restriction)
- When entering item titles or options, if you need to enter multiple values, use a semicolon as the separator, supporting both `；` and `;`.
- When naming theme music audio files or entering item titles, you can either input the title only or include year information. If there are multiple items with the same title but different years in the library, including year information helps the script automatically match the correct year of the item; otherwise, you will need to manually select it, and the format for adding years is `Item Title（Year）` or `Item Title (Year)`.
- When entering item titles, make sure that the titles you enter match the titles in the media library, otherwise, matching failures may occur. Do not use the delete key to delete characters during input, as it may cause recognition errors.
- Make sure the device running the script can connect to your server.
- Run the script with the X-Plex-Token of the server administrator account to ensure you have sufficient permissions.
