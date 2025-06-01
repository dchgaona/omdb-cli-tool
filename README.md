# OMDB CLI Tool

A command-line interface for searching and retrieving movie, TV series, and episode information from the Open Movie Database (OMDB) API.

## Features

- 🎬 Search for movies, TV series, and episodes
- 🔍 Get detailed information by title or IMDB ID
- 📊 Display ratings from multiple sources (IMDB, Rotten Tomatoes, Metacritic)
- 🎯 Filter by content type and year
- 📄 Configurable plot length (short or full)
- 📃 Paginated search results

## Prerequisites

- Python 3.6 or higher
- An OMDB API key (free at [omdbapi.com](http://www.omdbapi.com/apikey.aspx))

## Installation

1. Clone or download this repository
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your API key:
   ```
   API_KEY=your_omdb_api_key_here
   ```

## Usage

The tool operates in two main modes: **Search Mode** and **Lookup Mode**.

### Search Mode

Search for multiple results matching your criteria:

```bash
python app.py --search --title "Batman" --type movie --year 2008 --page 1
```

**Search Mode Arguments:**
- `--search` - Enable search mode
- `--title` - Movie/show title to search for (required)
- `--type` - Content type: `movie`, `series`, or `episode` (default: movie)
- `--year` - Release year filter (optional)
- `--page` - Page number for results (1-100, default: 1)

### Lookup Mode

Get detailed information about a specific title:

#### By Title
```bash
python app.py --title "The Dark Knight" --year 2008 --type movie --plot full
```

#### By IMDB ID
```bash
python app.py --imdb tt0468569 --plot short
```

**Lookup Mode Arguments:**
- `--title` - Movie/show title (alternative to --imdb)
- `--imdb` - IMDB ID (alternative to --title)
- `--type` - Content type: `movie`, `series`, or `episode` (default: movie)
- `--year` - Release year filter (optional)
- `--plot` - Plot length: `short` or `full` (default: short)

## Examples

### Search for Batman movies from 2008
```bash
python app.py --search --title "Batman" --type movie --year 2008
```

Output:
```
-------------------------------
1. Batman: Gotham Knight
Year: 2008
IMDB Id: tt1117563
...
-------------------------------
```

### Get detailed information about a specific movie
```bash
python app.py --title "Inception" --year 2010 --plot full
```

Output:
```
-------------------------------
Inception
Year: 2010, Runtime: 148 min, Genre: Action, Adventure, Sci-Fi
Dom Cobb is a skilled thief, the absolute best in the dangerous art of extraction, stealing valuable secrets from deep within the subconscious during the dream state, when the mind is at its most vulnerable. Cobb's rare ability has made him a coveted player in this treacherous new world of corporate espionage, but it has also made him an international fugitive and cost him everything he has ever loved. Now Cobb is being offered a chance at redemption. One last job could give him his life back but only if he can accomplish the impossible, inception. Instead of the perfect heist, Cobb and his team of specialists have to pull off the reverse: their task is not to steal an idea, but to plant one. If they succeed, it could be the perfect crime. But no amount of careful planning or expertise can prepare the team for the dangerous enemy that seems to predict their every move. An enemy that only Cobb could have seen coming.
Ratings:
	Rotten Tomatoes: 87%
	Metacritic: 74/100
------------------------------
-```

### Search for TV series
```bash
python app.py --search --title "Breaking Bad" --type series
```

### Get information using IMDB ID
```bash
python app.py --imdb tt0468569 --plot full
```

## Content Types

- **movie** - Feature films
- **series** - TV shows and miniseries

## Rating Display

The tool displays different ratings based on content type:

- **Movies**: Shows Rotten Tomatoes and Metacritic scores
- **TV Series**: Shows only IMDB rating (due to API limitations)

---

**Note**: This tool is not affiliated with or endorsed by the Open Movie Database.
