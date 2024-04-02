import os
import re
import shutil
import hashlib
import configparser
import plexapi.server
from pathlib import Path

def initialize_settings(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    plex_url = config.get('server', 'address')
    plex_token = config.get('server', 'token')
    metadata_base_directory = config.get('server', 'metadata_base_directory')
    language = config.get('server', 'language')
    continuous_mode = config.getboolean('mode', 'continuous_mode')
    user_theme = config.getboolean('mode', 'user_theme')
    plex_theme = config.getboolean('mode', 'plex_theme')

    plex_server = plexapi.server.PlexServer(baseurl=plex_url, token=plex_token)
    if language == 'zh':
        print(f"已成功连接到服务器：{plex_server.friendlyName}")
    elif language == 'en':
        print(f"Successfully connected to server: {plex_server.friendlyName}\n")
    return plex_server, metadata_base_directory, language, continuous_mode, user_theme, plex_theme

def _get_metadata_path(item, metadata_base_directory):
    metadata_type_map = {
        'movie': 'Movies',
        'show': 'TV Shows',
        'artist': 'Artists',
        'collection': 'Collections',
    }
    guid = item.guid
    full_hash = hashlib.sha1(guid.encode()).hexdigest()
    metadata_path = os.path.join(
        metadata_base_directory, metadata_type_map[item.type],
        full_hash[0], full_hash[1:] + '.bundle')
    return metadata_path

def delete_and_print(item, metadata_base_directory, language, user_theme, plex_theme, item_type_dict):
    if user_theme:
        theme_path = os.path.join(_get_metadata_path(item, metadata_base_directory), 'Uploads', 'themes')
        try:
            shutil.rmtree(theme_path)
        except FileNotFoundError:
            pass
    if plex_theme:
        theme_path = os.path.join(_get_metadata_path(item, metadata_base_directory), 'Contents', '_combined', 'themes')
        try:
            shutil.rmtree(theme_path)
        except FileNotFoundError:
            pass
    year_info = f" ({item.year})" if hasattr(item, 'year') else ""
    if language == 'zh':
        print(f"已成功删除 \"{item.librarySectionTitle}\" 中的{item_type_dict[item.type]} \"{item.title}{year_info}\" 的主题音乐")
    elif language == 'en':
        print(f"Successfully deleted theme music for {item_type_dict[item.type]} \"{item.title}{year_info}\" in \"{item.librarySectionTitle}\"")

def delete_themes(plex_server, item_title, item_year, config_file, metadata_base_directory, language, user_theme, plex_theme):
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
            if item.title == item_title and (not item_year or (hasattr(item, 'year') and item.year == item_year)):
                matched_items.append((item_type, item))

    if len(matched_items) == 0:
        if language == 'zh':
            print(f"未找到名为 \"{item_title}\" 的项目")
        elif language == 'en':
            print(f"No item titled \"{item_title}\" found")
        return
    elif len(matched_items) > 1:
        years = [item.year for _, item in matched_items if hasattr(item, 'year')]
        if len(set(years)) <= 1 or all(not hasattr(item, 'year') for _, item in matched_items):
            for item_type, item in matched_items:
                delete_and_print(item, metadata_base_directory, language, user_theme, plex_theme, item_type_dict)
        else:
            print()
            for i, (item_type, item) in enumerate(matched_items):
                year_info = f" ({item.year})" if hasattr(item, 'year') else ""
                if language == 'zh':
                    print(f"{i+1}. \"{item.librarySectionTitle}\" 中的{item_type_dict[item_type]}：{item.title}{year_info}")
                elif language == 'en':
                    print(f"{i+1}. {item_type_dict[item_type]} \"{item.title}{year_info}\" in \"{item.librarySectionTitle}\"")
            choices = input("\n请选择要删除主题音乐的项目（多个项目用分号隔开）：") if language == 'zh' else input("\nPlease select the item(s) from which you want to delete theme music (multiple items separated by semicolons): ")
            choices = [choice.strip() for choice in re.split(';|；', choices)]
            print()
            for choice in choices:
                choice = int(choice) - 1
                item_type, item = matched_items[choice]
                delete_and_print(item, metadata_base_directory, language, user_theme, plex_theme, item_type_dict)
    else:
        item_type, item = matched_items[0]
        delete_and_print(item, metadata_base_directory, language, user_theme, plex_theme, item_type_dict)

def main():
    config_file = Path(__file__).parent / 'config.ini'
    plex_server, metadata_base_directory, language, continuous_mode, user_theme, plex_theme = initialize_settings(config_file)

    while True:
        item_titles = input("\n请输入要删除主题音乐的项目名称（多个名称用分号隔开）：") if language == 'zh' else input("Please enter the title(s) of the item(s) from which you want to delete theme music (multiple names separated by semicolons): ")
        item_titles = [item.strip() for item in re.split(';|；', item_titles)]
        print()

        for item_title in item_titles:
            match = re.match(r"(.*?)\s*[\(\（](\d{4})[\)\）]", item_title.strip())
            if match:
                item_title, item_year = match.groups()
                item_year = int(item_year)
            else:
                item_year = None
            delete_themes(plex_server, item_title, item_year, config_file, metadata_base_directory, language, user_theme, plex_theme)

        if not continuous_mode:
            break

if __name__ == "__main__":
    main()
