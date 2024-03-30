import os
import re
import shutil
import configparser
import plexapi.server
from pathlib import Path

def initialize_settings(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    plex_url = config.get('server', 'address')
    plex_token = config.get('server', 'token')
    language = config.get('server', 'language')

    plex_server = plexapi.server.PlexServer(baseurl=plex_url, token=plex_token)
    if language == 'zh':
        print(f"已成功连接到服务器：{plex_server.friendlyName}\n")
    elif language == 'en':
        print(f"Successfully connected to server: {plex_server.friendlyName}\n")
    return plex_server, language

def upload_and_print(item, theme_path, item_type_dict, language):
    item.uploadTheme(filepath=theme_path)
    year_info = f" ({item.year})" if hasattr(item, 'year') else ""
    if language == 'zh':
        print(f"已成功为 \"{item.librarySectionTitle}\" 中的{item_type_dict[item.type]} \"{item.title}{year_info}\" 上传主题音乐")
    elif language == 'en':
        print(f"Successfully uploaded theme music for {item_type_dict[item.type]} \"{item.title}{year_info}\" in \"{item.librarySectionTitle}\"")

def upload_themes(plex_server, item_name, item_year, theme_path, config_file, first_file, language):
    config = configparser.ConfigParser()
    config.read(config_file)
    item_types = [item_type for item_type in ["movie", "show", "artist", "collection"] if config.getboolean('search', item_type)]
    item_type_chinese = {"movie": "电影", "show": "电视节目", "artist": "歌手", "collection": "合集"}
    item_type_english = {"movie": "Movie", "show": "TV Show", "artist": "Artist", "collection": "Collection"}

    item_type_dict = item_type_chinese if language == 'zh' else item_type_english

    matched_items = []
    for item_type in item_types:
        items = plex_server.library.all(libtype=item_type)
        for item in items:
            if item.title == item_name and (not item_year or (hasattr(item, 'year') and item.year == item_year)):
                matched_items.append((item_type, item))

    if len(matched_items) == 0:
        if language == 'zh':
            print(f"未找到名为 \"{item_name}\" 的项目")
        elif language == 'en':
            print(f"No item named \"{item_name}\" found")
        return
    elif len(matched_items) > 1:
        years = [item.year for _, item in matched_items if hasattr(item, 'year')]
        if len(set(years)) <= 1:
            for item_type, item in matched_items:
                upload_and_print(item, theme_path, item_type_dict, language)
        else:
            same_year_items = []
            printed_option = False
            for i, (item_type, item) in enumerate(matched_items):
                year_info = f" ({item.year})" if hasattr(item, 'year') else ""
                if not first_file and not printed_option:
                    print()
                if language == 'zh':
                    print(f"{i+1}. \"{item.librarySectionTitle}\" 中的{item_type_dict[item_type]}：{item.title}{year_info}")
                elif language == 'en':
                    print(f"{i+1}. {item_type_dict[item_type]} \"{item.title}{year_info}\" in \"{item.librarySectionTitle}\"")
                printed_option = True
            choices = input("\n请选择要添加主题音乐的项目（多个项目用分号隔开）：") if language == 'zh' else input("\nPlease select the item(s) to which you want to add theme music (multiple items separated by semicolons): ")
            choices = [choice.strip() for choice in re.split(';|；', choices)]
            print()
            for choice in choices:
                choice = int(choice) - 1
                item_type, item = matched_items[choice]
                upload_and_print(item, theme_path, item_type_dict, language)
    else:
        item_type, item = matched_items[0]
        upload_and_print(item, theme_path, item_type_dict, language)

def main():
    config_file = Path(__file__).parent / 'config.ini'
    plex_server, language = initialize_settings(config_file)

    config = configparser.ConfigParser()
    config.read(config_file)

    upload_dir = Path(__file__).parent / 'uploads'
    first_file = True
    for theme_file in os.listdir(upload_dir):
        if theme_file.startswith('.'):
            continue
        item_name, _ = os.path.splitext(theme_file)
        match = re.match(r"(.*?)\s*[\(\（](\d{4})[\)\）]", item_name)
        if match:
            item_name, item_year = match.groups()
            item_year = int(item_year)
        else:
            item_year = None
        theme_path = os.path.join(upload_dir, theme_file)
        upload_themes(plex_server, item_name, item_year, theme_path, config_file, first_file, language)
        first_file = False

        if config.getboolean('mode', 'delete_after_upload'):
            os.remove(theme_path)
        else:
            shutil.move(theme_path, os.path.join(Path(__file__).parent, 'themes'))

if __name__ == "__main__":
    main()
