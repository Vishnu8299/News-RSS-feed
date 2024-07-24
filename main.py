from flask import Flask, request, render_template, send_file
import requests
import feedparser
import json
import re

app = Flask(__name__)

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-\.]', '_', name)

def verify_rss_url(rss_url):
    try:
        response = requests.get(rss_url)
        if response.status_code != 200:
            return False, f"The URL did not return a successful response. Status code: {response.status_code}"

        content_type = response.headers.get('Content-Type', '')
        if 'xml' not in content_type.lower():
            return False, f"The URL does not seem to point to an RSS feed (Content-Type: {content_type})"

        feed = feedparser.parse(response.content)
        if feed.bozo:
            return False, "Failed to parse RSS feed. The URL may not be an RSS feed."

        feed_info = {
            'title': feed.feed.title,
            'link': feed.feed.link,
            'description': feed.feed.description,
            'entries': [],
            'total_entries': len(feed.entries)
        }

        for entry in feed.entries:
            entry_info = {
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'summary': entry.summary
            }
            # Check for common places where images might be stored in RSS entries
            if 'media_content' in entry and entry.media_content:
                entry_info['image'] = entry.media_content[0]['url']
            elif 'media_thumbnail' in entry and entry.media_thumbnail:
                entry_info['image'] = entry.media_thumbnail[0]['url']
            elif 'image' in entry:
                entry_info['image'] = entry.image
            elif 'enclosures' in entry and entry.enclosures:
                entry_info['image'] = entry.enclosures[0]['href']

            feed_info['entries'].append(entry_info)

        # Use the feed title as the file name
        file_name = sanitize_filename(feed.feed.title) + '.json'
        
        # Save feed_info to a JSON file
        with open(file_name, 'w') as json_file:
            json.dump(feed_info, json_file, indent=4)

        return True, file_name
    except requests.RequestException as e:
        return False, f"An error occurred while trying to fetch the URL: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rss_url = request.form['rss_url']
        is_valid, result = verify_rss_url(rss_url)
        if is_valid:
            return render_template('result.html', feed_info=result)  # Pass feed_info to the template
        else:
            return render_template('index.html', error=result)

    return render_template('index.html')

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
