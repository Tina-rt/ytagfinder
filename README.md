# YTagFinder

A simple python module to fetch all tags of an Youtube video from an url

## Requirements
- Python 3.5 or above

## Dependencies
- bs4

## Usage
```python
    from YTagFinder import YTagFinder
    ytag = YTagFinder()
    tags = ytag.find_tags('https://youtube_url')
```